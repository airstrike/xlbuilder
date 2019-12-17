# built-in libraries
import argparse, ast, datetime, glob, itertools, logging, os, re, shutil, sys, tempfile
from collections import OrderedDict
from io import BytesIO
from types import SimpleNamespace
import xml.etree.ElementTree as ET

# third-party libraries
from utils import handle_exceptions, UpdateableZipFile
from bs4 import BeautifulSoup
import win32com.client
import yaml

from logger import logger
from pywintypes import com_error

# TODO: Check if customUI14base.py requires us to sanitize inputs for ids. If so, either
# monkey-patch the original classes or make them subclass from a BaseElement class that
# sanitizes inputs
def sanitize_id(text):
    pattern = re.compile('[\W_]+', re.UNICODE)
    return pattern.sub('', text)

FILE_FORMAT = {
    # https://docs.microsoft.com/en-us/office/vba/api/excel.xlfileformat
    51: '.xlsx', # xlOpenXMLWorkbook
    52: '.xlsm', # xlOpenXMLWorkbookMacroEnabled
    55: '.xlam', # xlOpenXMLAddin

    # Not really the same as the Ribbon XML but hey, it works
    46: '.xml', # xlXMLSpreadsheet
}

TEMPLATE_CALLBACK = """
Sub call{fun}(control as IRibbonControl)
    Call {fun}
End Sub
"""

class XLSMBuilder(object):
    XL = None
    WB = None
    XlFileFormat = '52'
    input = './src/*.*'
    output = 'XLSMBuilderFile'
    dry = False
    dry_msg = ''
    vb_references = []

    @property
    def extension(self):
        return FILE_FORMAT.get(self.XlFileFormat, None)

    @property
    def full_file_path(self):
        return os.path.normpath(os.path.join(os.getcwd(), os.path.splitext(self.output)[0] + self.extension))

    @property
    def source_file_list(self):
        return itertools.chain(*[glob.glob(x) for x in self.input])

    def __init__(self, *args, **kwargs):
        super(XLSMBuilder, self).__init__()
        self.tags = kwargs.get('tags', {})
        self.input = kwargs.get('input', self.input)
        self.output = kwargs.get('output', self.output)
        self.dry = kwargs.get('dry', self.dry)
        self.register_pattern = re.compile("^'@register\((.*)\)")
        if self.dry: self.dry_msg = '(not really due to dry run)'

    @handle_exceptions
    def build(self, callback=None):
        logger.debug(f'Opening Excel {self.dry_msg}')
        logger.debug(f'Creating Workbook {self.dry_msg}')
        if not self.dry:
            self.XL = win32com.client.DispatchEx('Excel.Application')
            self.XL.Visible = False
            self.XL.Application.DisplayAlerts = False
            self.WB = self.XL.Workbooks.Add()

        logger.debug(f'Adding modules from {self.input}')
        for x, eachfilepath in enumerate(self.source_file_list):
            (file_path, file_name) = os.path.split(eachfilepath)
            with open(eachfilepath, 'rt') as eachfile:
                if not self.dry:
                    eachmodule = self.WB.VBProject.VBComponents.Add(1)
                else:
                    eachmodule = SimpleNamespace(Name=file_name[:-4])
                if not self.dry:
                    eachmodule.CodeModule.AddFromFile(eachfilepath)
                logger.info(f'Added {eachfilepath} as {eachmodule.Name}')

                for i, line in enumerate(eachfile):
                    ref_match  = self.register_pattern.match(line)

                    if ref_match:
                        reference = ast.literal_eval(ref_match.group(1))
                        if reference not in self.vb_references:
                            self.vb_references.append(reference)

        for reference in self.vb_references:
            self.WB.VBProject.References.AddFromGuid(*reference)

        if callback is not None: callback()

    def __enter__(self):
        return self

    def save(self):
        if not self.dry:
            try:
                self.WB.SaveAs(self.full_file_path, self.XlFileFormat)
                logger.info(f'Saved output file: {self.full_file_path} {self.dry_msg}')
            except com_error:
                logger.error(f'Error saving output file: {self.full_file_path}')
        else:
            logger.info(f'Saved output file: {self.full_file_path} {self.dry_msg}')

    def close(self):
        if not self.dry:
            try:
                self.WB.Close()
                logger.debug(f'Quitting Excel {self.dry_msg}')
            except com_error:
                logger.error(f'Error quitting Excel')
        else:
            logger.debug(f'Quitting Excel {self.dry_msg}')

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()
        self.close()
        if not self.dry:
            self.XL.Application.Quit()
            del self.XL


class XLAMBuilder(XLSMBuilder):
    XlFileFormat = 55
    ribbon = {}
    keep_xml = False
    ribbon_callbacks = []

    @property
    def ribbon_file_path(self):
        return os.path.normpath(os.path.splitext(self.output)[0] + '.xml')

    @property
    def ribbon_callbacks_as_string(self):
        s = """Attribute VB_Name = "Callbacks"\r\nOption Explicit"""
        s += "\r\n".join([TEMPLATE_CALLBACK.format(fun=i) for i in self.ribbon_callbacks])
        return s

    def __init__(self, *args, **kwargs):
        self.keep_xml = kwargs.get('keep_xml', self.keep_xml)
        self.ribbon = kwargs.get('ribbon', self.ribbon)
        if os.path.exists(self.ribbon_file_path):
            os.remove(self.ribbon_file_path)
        self.tag_pattern = re.compile("^'@ribbon\((.*)\)")
        self.sub_pattern = re.compile('^(?:Public |Private )?(?:Sub )(.*)(?:\((?:.*)?\))')
        super(XLAMBuilder, self).__init__(*args, **kwargs)

    def build(self, callback=None):
        super(XLAMBuilder, self).build()
        logger.info(f'Looking for ribbon tags in {"(" + ", ".join(self.input) + ")" if len(self.input) > 1 else self.input[0]}')
        for x, eachfilepath in enumerate(self.source_file_list):
            (file_path, file_name) = os.path.split(eachfilepath)
            with open(eachfilepath, 'rt') as eachfile:
                tag_dict = {}
                for i, line in enumerate(eachfile):
                    tag_match = self.tag_pattern.match(line)
                    sub_match = self.sub_pattern.match(line)
                    if tag_match:
                        tag_dict = ast.literal_eval(tag_match.group(1))

                    elif tag_dict is not {}: # meaning the last line was a tag
                        tag_dict['button_id'] = make_id(tag_dict.get('button_id', f'btn{sub_match.group(1)}'))
                        tag_dict['group_id'] = make_id(tag_dict.get('group_id', f'{tag_dict["group"]}Group'))
                        tag_dict['tab'] = make_id(tag_dict['tab'])
                        tag_dict['size'] = tag_dict.get('size', 'normal')

                        ribbon_tab_path = f"./ribbon/tabs/tab[@id='{tag_dict['tab']}']"
                        tab = self.ribbon.find(ribbon_tab_path)

                        # if no tab has yet been created (e.g. none provided in config file)
                        # create a basic tab matching this id
                        if tab is None:
                            tabs = self.ribbon.find("./ribbon/tabs")
                            tab = ET.SubElement(tabs, 'tab', attrib={
                                'id': make_id(tag_dict['tab']),
                                'label': tag_dict['tab'],
                                'keytip': '/',
                                'insertAfterMso': 'TabView',
                            })

                        # if this is the first tag matching this group and tab, check that the
                        # group exists and create it if it doesn't
                        group = tab.find(f"group[@id='{tag_dict['group_id']}']")
                        if group is None:
                            group = ET.SubElement(tab, 'group', attrib={
                                'id': make_id(tag_dict['group_id']),
                                'label': tag_dict['group'],
                            })

                        button_attribs = {
                            'id': make_id(tag_dict['button_id']),
                            'label': tag_dict['label'],
                            'imageMso': tag_dict['image'],
                            'size': tag_dict['size'],
                            'keytip': tag_dict['keytip'],
                            'onAction': f"call{sub_match.group(1)}",
                        }
                        if tag_dict.get('screentip', None) is not None:
                            button_attribs['screentip'] = tag_dict.get('screentip')
                        ET.SubElement(group, 'button', attrib=button_attribs)
                        self.ribbon_callbacks.append(f'{sub_match.group(1)}')

                        tag_dict = None
                        tag_match = None

                logger.info(f'Parsed {eachfilepath}')

        contextualtabs = self.ribbon.find('./ribbon/contextualtabs')
        ribbon = self.ribbon.find('./ribbon')
        if contextualtabs.text is None:
            ribbon.remove(contextualtabs)

        f = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        f.write(self.ribbon_callbacks_as_string)
        file_name = f.name
        f.close()
        if not self.dry:
            callbacks_module = self.WB.VBProject.VBComponents.Add(1)
            callbacks_module.CodeModule.AddFromFile(file_name)
        os.remove(file_name)

        self.ribbon.write(self.ribbon_file_path, encoding='utf-8', xml_declaration=True)
        if self.keep_xml:
            logger.debug(f"Saved ribbon file to {self.ribbon_file_path}")

        if callback is not None: callback()

    def save(self):
        super(XLAMBuilder, self).save()

        logger.debug(f"Opening output file {self.full_file_path} {self.dry_msg}")
        if not self.dry:
            with UpdateableZipFile(self.full_file_path, 'a') as output:
                with output.open('_rels/.rels', 'r') as rels:
                    ET.register_namespace("", "http://schemas.openxmlformats.org/package/2006/relationships")
                    tree = ET.parse(rels)
                    relationships = [i for i in tree.iter()][0] #FIXME: use namespace
                    ET.SubElement(relationships, 'Relationship', attrib={
                        'Id': 'xlbuilder',
                        'Type': "http://schemas.microsoft.com/office/2007/relationships/ui/extensibility",
                        'Target': '/customUI/customUI14.xml',
                    })
                    # sadly, ET.tostring() doesn't include an XML declaration
                    # otherwise one could simply...
                    # output.writestr('_rels/.rels', ET.tostring(root))
                    # unless you append .encoding('utf8') to that function, in which case
                    # it does include a declaration but 'utf8' isn't valid XML, but 'UTF-8' is
                    f = BytesIO()
                    tree.write(f, encoding='utf-8', xml_declaration=True)
                    output.writestr('_rels/.rels', f.getvalue())
                output.write(self.ribbon_file_path, 'customUI/customUI14.xml')
            if not self.keep_xml:
                os.unlink(self.ribbon_file_path)

    def add_ribbon(self, ribbon):
        pass

def run():
    # Load arguments from command line
    argsformatter = lambda prog: argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=100, width=100)
    parser = argparse.ArgumentParser(prog="xlbuilder.py", formatter_class=argsformatter) #argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('output', nargs='?', default='XLSMBuilder', help='name of output file')
    parser.add_argument('input', nargs='*', default='src', help='location of source file(s), accepts wildcards')
    parser.add_argument('--config', '-c', dest='config', default='config.yml',
            help='optional config file')
    parser.add_argument('--type', default='xlam', choices=['xlam', 'xlsm'],
            help='Type of output to be built')
    parser.add_argument('--dry', '-d', action='store_true', default=False,
            help="dry run (does not launch Excel or create output)")
    parser.add_argument('--keep_xml', action='store_true', default=False)
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    # Load arguments from config file if provided and readable
    config = {}
    try:
        with open(args.config, 'r') as ymlfile:
            config = yaml.safe_load(ymlfile)

    except FileNotFoundError:
        config = {}


    xml = ET.ElementTree(ET.fromstring('<customUI><ribbon><tabs></tabs><contextualtabs></contextualtabs></ribbon></customUI>'))
    for customUI in xml.iter('customUI'):
        customUI.set('xmlns', 'http://schemas.microsoft.com/office/2006/01/customui')
    tabs = [i for i in xml.iter('tabs')][0]
    contextualtabs = [i for i in xml.iter('contextualtabs')][0]

    for key, values in config.get('ribbon', {}).items():
        values['id'] = values.get('id', ''.join(key.split()))
        if values.get('type') == 'chart':
            parent = contextualtabs.find("tabSet[idMso='TabSetChartTools']")
            if parent is None:
                parent = ET.SubElement(contextualtabs, 'tabSet', attrib={'idMso': 'TabSetChartTools'})
        else:
            parent = tabs
            values['label'] = values.get('label', values.get('id', ''))
            values['insertAfterMso'] = values.get('after', 'TabView')

        # remove extraneous attributes
        for v in ('after', 'type'):
            try:
                values.pop(v)
            except KeyError:
                pass

    context = {
        'config': config,
        'verbose': config.get('verbose', args.verbose),
        'dry': config.get('dry', args.dry),
        'type': config.get('type', args.type),
        'output': config.get('output', args.output),
        'input': config.get('input', args.input),
        'tags': config.get('tags', {}),
        'ribbon': xml,
    }

    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels)-1, context['verbose'])]
    logger.setLevel(level)

    if context['dry']:
        logger.warning('!!! Dry run (does not launch Excel or create any files) !!!')

    if config == {}:
        logger.warning(f'Could not find {args.config} config file. Running with defaults and CLI arguments only')
    else:
        logger.info(f'Loaded config from {args.config} file')

    # Sanitize input
    # ensure input is a list of directories or files
    if not isinstance(context['input'], (list, tuple)):
        context['input'] = [context['input']]

    # user may have provided just the directory name rather than a fullpath
    context['input'] = [
            os.path.normpath(os.path.join(os.getcwd(), '.', x))
            for x in context['input']
    ]

    # user may or may not have provided a matching wildcard, in which case we add one
    context['input'] = [
            os.path.join(x, '*.*') if os.path.isdir(x) else x
            for x in context['input']
    ]

    # normalize every path for OCD reasons
    context['input'] = [os.path.normpath(x) for x in context['input']]

    # Instantiate and run the correct builder
    if context['type'] == 'xlam':
        context.update({'keep_xml': config.get('keep_xml', args.keep_xml)})
        with XLAMBuilder(**context) as builder:
            builder.build()

    if context['type'] == 'xlsm':
        with XLSMBuilder(**context) as builder:
            builder.build()

if __name__ == '__main__':
    run()
