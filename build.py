﻿# build-in libraries
from pprint import pprint as p #TODO: removeme
import argparse, ast, copy, datetime, glob, itertools, logging, os, re, sys
from collections import OrderedDict
from types import SimpleNamespace
import xml.etree.ElementTree as ET

# third-party libraries
import colorful
import win32com.client
import yaml

# inspired by
# http://uran198.github.io/en/python/2016/07/12/colorful-python-logging.html
with colorful.with_16_ansi_colors() as c:
    LOG_COLORS = {
        logging.ERROR: c.on_red,
        logging.WARNING: c.on_yellow,
        logging.DEBUG: c.on_cyan,
        logging.CRITICAL: c.on_magenta,
        logging.INFO: c.on_blue,
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
                    new_record.levelname = f'{c.bold}{levelcolor} {levelname:<9}{c.reset}'
                else:
                    new_record.levelname = f'{c.bold}{c.reset}{levelcolor}          {c.reset}'
            self.last_levelno = new_record.levelno
            return super(ColorFormatter, self).format(new_record, *args, **kwargs)

formatter = ColorFormatter("%(levelname)s %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

# boilerplate helper functions
rel = lambda *x: os.path.join('.', *x)

FILE_FORMAT = {
    # https://docs.microsoft.com/en-us/office/vba/api/excel.xlfileformat
    51: '.xlsx', # xlOpenXMLWorkbook
    52: '.xlsm', # xlOpenXMLWorkbookMacroEnabled
    55: '.xlam', # xlOpenXMLAddin

    # Not really the same as the Ribbon XML but hey, it works
    46: '.xml', # xlXMLSpreadsheet
}

class XLBuilder(object):
    XL = None
    WB = None
    working_dir = '.'
    input_files = './src/*.*'
    XlFileFormat = None # implement in subclass
    output_file = 'XLBuilderFile'
    dry = False # dry run?
    dry_msg = ''

    @property
    def extension(self):
        return FILE_FORMAT.get(self.XlFileFormat, None)

    @property
    def full_file_path(self):
        return os.path.normpath(os.path.splitext(self.output_file)[0] + self.extension)

    @property
    def source_file_list(self):
        return itertools.chain(*[glob.glob(x) for x in self.input_files])

    def __init__(self, *args, **kwargs):
        super(XLBuilder, self).__init__()
        self.tags = kwargs.get('tags', {})
        self.working_dir = kwargs.get('working_dir', self.working_dir)
        self.input_files = kwargs.get('input_files', self.input_files)
        self.output_file = kwargs.get('output_file', self.output_file)
        self.dry = kwargs.get('dry', self.dry)
        if self.dry: self.dry_msg = '(not really due to dry run)'

    def build(self, callback=None):
        logger.debug(f'Opening Excel {self.dry_msg}')
        logger.debug(f'Creating Workbook {self.dry_msg}')
        if not self.dry:
            self.XL = win32com.client.DispatchEx('Excel.Application')
            self.XL.Visible = False
            self.XL.Application.DisplayAlerts = False
            self.WB = self.XL.Workbooks.Add()

        logger.debug(f'Adding files from {self.input_files}')
        for x, eachfilepath in enumerate(self.source_file_list):
            (file_path, file_name) = os.path.split(eachfilepath)
            with open(eachfilepath, 'rt') as eachfile:
                tag_dict = None
                if not self.dry:
                    eachmodule = self.WB.VBProject.VBComponents.Add(1)
                else:
                    eachmodule = SimpleNamespace(Name=file_name[:-4])
                for i, line in enumerate(eachfile):
                    linestrip = line.strip() #TODO: remove if not needed
                    line_length = len(line) #TODO: remove if not needed
                    tag_match = self.tag_pattern.match(line)
                    sub_match = self.sub_pattern.match(line)
                    if tag_match:
                        tag_dict = ast.literal_eval(tag_match.group(1))
                        logger.debug(f'Matches {tag_dict}')

                    # if sub_match: # tag_dict is not None: # meaning the last line was a tag
                    elif tag_dict is not None: logger.debug(f'Sub {sub_match.group(0)}')
                        #TODO: do something with tags

                    tag_dict = None
                    tag_match = None

                if not self.dry: eachmodule.CodeModule.AddFromFile(eachfilepath)
                logger.info(f'Adding {eachfilepath} as {eachmodule.Name}')

        if callback is not None: callback()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.dry: self.WB.SaveAs(self.full_file_path, self.XlFileFormat)
        logger.info(f'Saved output file: {self.full_file_path} {self.dry_msg}')
        if not self.dry: self.WB.Close()
        logger.debug(f'Quitting Excel {self.dry_msg}')
        if not self.dry:
            self.XL.Application.Quit()
            del self.XL

class XLSMBuilder(XLBuilder):
    XlFileFormat = '52'

class XLAMBuilder(XLBuilder):
    XlFileFormat = 55

    def __init__(self, *args, **kwargs):
        self.output_file = kwargs.get('output_file', self.output_file)
        self.tag_pattern = re.compile("^'@register\((.*)\)")
        self.sub_pattern = re.compile('^(?:Sub )(.*)(?:\((?:.*)?\))')

        super(XLAMBuilder, self).__init__(*args, **kwargs)
        self.build_ribbon()

    def build(self, callback=None):
        super(XLAMBuilder, self).build(self.build_ribbon)

    def build_ribbon(self, *args, **kwargs):
        logger.debug('Initiating ribbon build')

    def add_ribbon(self, ribbon):
        pass

class RibbonButton(OrderedDict):
    def __missing__(self, key):
        if key == 'btnid':
            return self['label'] + '__id'
        raise KeyError(key)

def run():
    # Load arguments from command line
    argsformatter = lambda prog: argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=100, width=100)
    parser = argparse.ArgumentParser(prog="xlbuilder.py", formatter_class=argsformatter) #argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('output_file', nargs='?', default='XLBuilder', help='name of output file')
    parser.add_argument('input_files', nargs='*', default='src', help='path to source files, accepts wildcards')
    parser.add_argument('--config', '-c', dest='config', default='config.yml',
            help='optional config file')
    parser.add_argument('--type', default='xlam', choices=['xlam', 'xlsm'],
            help='Type of output_file to be built')
    parser.add_argument('--dry', '-d', action='store_true', default=False,
            help="dry run (does not launch Excel or create output_file)")
    parser.add_argument('--verbose', '-v', action='count', default=0)
    args = parser.parse_args()

    # Load arguments from config file if provided and readable
    config = {}
    try:
        with open(args.config, 'r') as ymlfile:
            config = yaml.safe_load(ymlfile)

    except FileNotFoundError:
        config = {}

    context = {
        'config': config,
        'verbose': config.get('verbose', args.verbose),
        'dry': config.get('dry', args.dry),
        'type': config.get('type', args.type),
        'output_file': config.get('output', args.output_file),
        'input_files': config.get('input', args.input_files),
        'tags': config.get('tags', {}),
        'ribbon': config.get('ribbon', {}),
    }

    levels = [logging.INFO, logging.DEBUG]
    level = levels[min(len(levels)-1, context['verbose'])]
    logger.setLevel(level)
    logger.debug('Running as main program')

    if context['dry']:
        logger.warning('!!! Dry run (does not launch Excel or create any files) !!!')

    if config == {}:
        logger.warning(f'Could not find {args.config} config file. Running with defaults and CLI arguments only')
    else:
        logger.info(f'Loaded config from {args.config} file')

    # Sanitize input_files
    # ensure input_files is a list of directories or files
    if not isinstance(context['input_files'], (list, tuple)):
        context['input_files'] = [context['input_files']]

    # user may have provided just the directory name rather than a fullpath
    context['input_files'] = [
            os.path.normpath(rel('.', x))
            for x in context['input_files']
    ]

    # user may or may not have provided a matching wildcard, in which case we add one
    context['input_files'] = [
            os.path.join(x, '*.*') if os.path.isdir(x) else x
            for x in context['input_files']
    ]

    # normalize every path for OCD reasons
    context['input_files'] = [os.path.normpath(x) for x in context['input_files']]

    # Instantiate and run the correct builder
    if context['type'] == 'xlam':
        with XLAMBuilder(**context) as builder:
            builder.build()

    if context['type'] == 'xlsm':
        with XLSMBuilder(**context) as builder:
            builder.build()

if __name__ == '__main__':
    run()
