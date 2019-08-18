# build-in libraries
from pprint import pprint as pp, pformat as pf #TODO: removeme
import argparse, ast, copy, datetime, glob, itertools, logging, os, re, shutil, sys, tempfile
from collections import OrderedDict
from functools import wraps
from io import BytesIO
from types import SimpleNamespace
import xml.etree.ElementTree as ET

# third-party libraries
from utils import UpdateableZipFile
from bs4 import BeautifulSoup
import colorful
import win32com.client
from pywintypes import com_error
import yaml

# inspired by
# http://uran198.github.io/en/python/2016/07/12/colorful-python-logging.html
with colorful.with_16_ansi_colors() as c:
    LOG_COLORS = {
        logging.ERROR: c.red,
        logging.WARNING: c.yellow,
        logging.DEBUG: c.cyan,
        logging.CRITICAL: c.magenta,
        logging.INFO: c.green,
    }

class ColorFormatter(logging.Formatter):
    last_levelno = None

    def format(self, record, *args, **kwargs):
        with colorful.with_8_ansi_colors() as c:
            # if the corresponding logger has children, they may receive modified
            # record, so we want to keep it intact
            new_record = copy.copy(record)
            if new_record.levelno in LOG_COLORS.keys():
                levelcolor = LOG_COLORS[new_record.levelno]
                # hide level name for repeated log messages with the same level
                if new_record.levelno != self.last_levelno:
                    levelname = new_record.levelname
                    new_record.levelname = f'{levelcolor}{levelname:<9}{c.reset}'
                else:
                    new_record.levelname = f'{c.reset}{levelcolor}         {c.reset}'
            self.last_levelno = new_record.levelno
            return super(ColorFormatter, self).format(new_record, *args, **kwargs)

formatter = ColorFormatter("%(levelname)s %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

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

# from https://stackoverflow.com/questions/23218974/wrapping-class-method-in-try-except-using-decorator
def handle_exceptions(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        try:
            return fn(self, *args, **kwargs)
        except com_error as e:
            exception_handler(e)
    return wrapper

def exception_handler(e):
    if e.excepinfo[5] == '-2147352567':
        logger.error(f'Path not found.')
        logger.error(f'{self.config}')

    else:
        logger.error(e)

class XLBuilder(object):
    XL = None
    WB = None
    XlFileFormat = None # implement in subclass
    input = './src/*.*'
    output = 'XLBuilderFile'
    dry = False
    dry_msg = ''

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
        super(XLBuilder, self).__init__()
        self.tags = kwargs.get('tags', {})
        self.input = kwargs.get('input', self.input)
        self.output = kwargs.get('output', self.output)
        self.dry = kwargs.get('dry', self.dry)
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

        if callback is not None: callback()

    def __enter__(self):
        return self

    def save(self):
        if not self.dry:
            try:
                self.WB.SaveAs(self.full_file_path, self.XlFileFormat)
                logger.info(f'Saved output file: {self.full_file_path} {self.dry_msg}')
            except com_error as e:
                logger.error(f'Error saving output file: {self.full_file_path}')
        else:
            logger.info(f'Saved output file: {self.full_file_path} {self.dry_msg}')

    def close(self):
        if not self.dry:
            try:
                self.WB.Close()
                logger.debug(f'Quitting Excel {self.dry_msg}')
            except com_error as e:
                logger.error(f'Error quitting Excel')
        else:
            logger.debug(f'Quitting Excel {self.dry_msg}')

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()
        self.close()
        if not self.dry:
            self.XL.Application.Quit()
            del self.XL

class XLSMBuilder(XLBuilder):
    XlFileFormat = '52'

class XLAMBuilder(XLBuilder):
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
        self.tag_pattern = re.compile("^'@register\((.*)\)")
        self.sub_pattern = re.compile('^(?:Sub )(.*)(?:\((?:.*)?\))')
        super(XLAMBuilder, self).__init__(*args, **kwargs)

    def build(self, callback=None):
        super(XLAMBuilder, self).build()
        logger.debug(f'Parsing ribbon tags from {self.input}')
        for x, eachfilepath in enumerate(self.source_file_list):
            (file_path, file_name) = os.path.split(eachfilepath)
            with open(eachfilepath, 'rt') as eachfile:
                tag_dict = None
                for i, line in enumerate(eachfile):
                    tag_match = self.tag_pattern.match(line)
                    sub_match = self.sub_pattern.match(line)
                    if tag_match:
                        tag_dict = ast.literal_eval(tag_match.group(1))

                    elif tag_dict is not None: # meaning the last line was a tag
                        tag_dict['tab_id'] = tag_dict.get('', f'{sub_match.group(1)}Tab')
                        tag_dict['button_id'] = tag_dict.get('', f'btn{sub_match.group(1)}')
                        tag_dict['group_id'] = tag_dict.get('group_id', f'{tag_dict["group"]}Group')
                        tag_dict['size'] = tag_dict.get('size', 'normal')

                        ribbon_tab_path = f"./ribbon/tabs/tab/[@id='{tag_dict['tab']}Tab']"
                        tab = self.ribbon.find(ribbon_tab_path)

                        # if no tab has yet been created (e.g. none provided in config file)
                        # create a basic tab matching this id
                        if tab is None:
                            tabs = self.ribbon.find("./ribbon/tabs")
                            tab = ET.SubElement(tabs, 'tab', attrib={
                                'id': tag_dict['tab_id'],
                                'label': tag_dict['tab'],
                                'keytip': '/',
                                'insertAfterMso': 'TabView',
                            })

                        # if this is the first tag matching this group and tab, check that the
                        # group exists and create it if it doesn't
                        group = tab.find(f"group[@id='{tag_dict['group_id']}']")
                        if group is None:
                            group = ET.SubElement(tab, 'group', attrib={
                                'id': tag_dict['group_id'],
                                'label': tag_dict['group'],
                            })

                        ET.SubElement(group, 'button', attrib={
                            'id': tag_dict['button_id'],
                            'label': tag_dict['label'],
                            'imageMso': tag_dict['image'],
                            'size': tag_dict['size'],
                            'keytip': tag_dict['keytip'],
                            'onAction': f"call{sub_match.group(1)}",

                        })
                        self.ribbon_callbacks.append(f'{sub_match.group(1)}')

                        tag_dict = None
                        tag_match = None

                logger.info(f'Parsed {eachfilepath}')

        logger.critical(f'{self.ribbon_callbacks_as_string}')
        f = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        f.write(self.ribbon_callbacks_as_string)
        file_name = f.name
        f.close()
        if not self.dry:
            callbacks_module = self.WB.VBProject.VBComponents.Add(1)
            callbacks_module.CodeModule.AddFromFile(file_name)
        os.remove(file_name)

        self.ribbon.write(open(self.ribbon_file_path, 'w'), encoding='unicode')
        bs = BeautifulSoup(open(self.ribbon_file_path), 'html.parser')
        with open(self.ribbon_file_path, 'w') as f:
            f.write(bs.prettify())
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
                    root = tree.getroot()
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
                    output.writestr('_rels/.rels', f.getvalue()) # ET.tostring(root))#, encoding='UTF-8'))
                    logger.debug('Updated .rels file to include reference to ribbon')
                output.write(self.ribbon_file_path, 'customUI/customUI14.xml')
                logger.debug(f"Added ribbon as /customUI/customUI14.xml")

    def add_ribbon(self, ribbon):
        pass

def run():
    # Load arguments from command line
    argsformatter = lambda prog: argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=100, width=100)
    parser = argparse.ArgumentParser(prog="xlbuilder.py", formatter_class=argsformatter) #argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('output', nargs='?', default='XLBuilder', help='name of output file')
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
            values['insertAfterMso'] = values.get('after', 'TabView')

        # remove extraneous attributes
        for v in ('after', 'type'):
            try:
                values.pop(v)
            except KeyError:
                pass

        element = ET.SubElement(parent, 'tab', attrib=values)

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
    logger.debug('Running as main program')

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
        context.update({'keep_xml': config.get('keep_xml', args.dry)})
        with XLAMBuilder(**context) as builder:
            builder.build()

    if context['type'] == 'xlsm':
        with XLSMBuilder(**context) as builder:
            builder.build()

if __name__ == '__main__':
    run()
    # input("Press the <ENTER> key to continue...")
