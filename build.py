import copy, datetime, glob, io, logging, os, re, sys
import xml.etree.ElementTree as ET

import colorama
from colorama import init as colorama_init
colorama_init()
import colorful
import win32com.client

# with colorful.with_8_ansi_colors() as c:
    # print(c.on_red('I am red'))

# inspired by
# http://uran198.github.io/en/python/2016/07/12/colorful-python-logging.html
# modified by yours truly
with colorful.with_8_ansi_colors() as c:
    LOG_COLORS = {
        logging.ERROR: c.on_red,
        logging.WARNING: c.on_yellow,
        logging.DEBUG: c.on_green,
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
                    new_record.levelname = f'{c.bold}{levelcolor} {levelname: ^10}{c.reset} '
                else:
                    new_record.levelname = f'{c.bold}{c.reset}           {levelcolor} {c.reset}'
            self.last_levelno = new_record.levelno
            return super(ColorFormatter, self).format(new_record, *args, **kwargs)

formatter = ColorFormatter("%(levelname)s %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

TAGS = {
    'Name':     'Terra Add-in',
    'Author':   'Andy Terra',
    'E-mail':   'andy@andyterra.com',
    'Website':  'https://excel.andyterra.com',
    'Version':  '0.3.1',
    'Timestamp': datetime.datetime.now().strftime('%c'),
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
rel = lambda *x: os.path.join(BASE_DIR, *x)

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
    working_dir = BASE_DIR
    source_file_dir = rel(BASE_DIR, 'src')
    XlFileFormat = None # implement in subclass
    file_name = 'XLBuilderFile'

    dry = False # dry run?

    @property
    def extension(self):
        return FILE_FORMAT.get(self.XlFileFormat, None)

    @property
    def file_name_with_extension(self):
        return self.file_name + self.extension

    @property
    def full_file_path(self):
        return rel(self.working_dir, self.file_name_with_extension)

    @property
    def source_files(self, match='ChartHelper.bas'):
        return glob.glob(os.path.join(self.source_file_dir, match))


    def __init__(self, *args, **kwargs):
        super(XLBuilder, self).__init__()
        logger.info('Initiating build %s (%s)' % (
            TAGS['Version'], TAGS['Timestamp']))
        self.working_dir = kwargs.get('working_dir', self.working_dir)
        self.dry = kwargs.get('dry', self.dry)
        logger.info('Working dir: %s' % self.working_dir)
        logger.debug('Opening Excel')
        logger.debug('Creating Workbook')
        logger.debug(f'self.dry = {self.dry}')
        if not self.dry:
            self.XL = win32com.client.DispatchEx('Excel.Application')
            self.XL.Visible = False
            self.XL.Application.DisplayAlerts = False
            self.WB = self.XL.Workbooks.Add()
        self.add_files()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logger.debug('Saving Workbook: %s' % self.full_file_path)
        self.WB.SaveAs(self.full_file_path, self.XlFileFormat)
        logger.debug('Closing Workbook')
        self.WB.Close()
        logger.debug('Quitting Excel')
        self.XL.Application.Quit()
        del self.XL

    def add_files(self):
        logger.debug(f'Adding modules from {self.source_file_dir}')
        for x, eachfilepath in enumerate(self.source_files):
            logger.debug('Adding script file: %s' % eachfilepath)
            (file_path, file_name) = os.path.split(eachfilepath)
            if not self.dry:
                with io.open(eachfilepath, 'rt', newline='\n') as eachfile:
                    eachmodule = self.WB.VBProject.VBComponents.Add(1)
                    for i, line in enumerate(eachfile):
                        linestrip = line.strip()
                        line_length = len(line)
                        tag_match = self.tag_pattern.match(line)
                        attribute_match = self.attribute_pattern.match(line)
                        vbname_match = self.vbname_pattern.match(line)
                        if tag_match:
                            logger.debug(f'Matches {tag_match.group(1)}')
                        elif vbname_match:
                            if file_name == 'ChartHelper.bas' and i < 20: logger.debug(f'VBName Match: {linestrip}')
                            eachmodule.Name = vbname_match.group(1)
                            logger.critical(f'Renamed  model to {vbname_match.group(1)}')
                        elif attribute_match:
                            if file_name == 'ChartHelper.bas' and i < 20: logger.debug(f'Attr Match:   {linestrip}')
                            # logger.critical(f'Matches {attribute_match.group(1)}')
                            z = 1 # must skip attributes if we're using AddFromString
                            eachmodule.CodeModule.AddFromString("'Attribute match    \r\n")
                        elif not line.strip():
                            if file_name == 'ChartHelper.bas' and i < 20: logger.debug(f"Empty {line_length}:   '{linestrip}'")
                            eachmodule.CodeModule.AddFromString("'Empty line    \r\n")
                        else:
                            if file_name == 'ChartHelper.bas' and i < 20: logger.debug(f'Else {line_length}:   {linestrip}')
                            # if file_name == 'ChartHelper': logger.critical(f'Matches {attribute_match.group(1)}')
                            eachmodule.CodeModule.AddFromString(line)


class XLAMBuilder(XLBuilder):
    XlFileFormat = 55
    file_name = 'ribbon'

    def __init__(self, *args, **kwargs):
        self.tag_pattern = re.compile("^'@register\((.*)\)$")
        self.attribute_pattern = re.compile("^Attribute (.*)$")
        self.vbname_pattern = re.compile('^Attribute VB_Name = "(.*)".*$')
        super(XLAMBuilder, self).__init__(*args, **kwargs)
        self.build_ribbon()

    def build_ribbon(self, *args, **kwargs):
        logger.debug('Initiating ribbon build')

    def add_ribbon(self, ribbon):
        pass

def run():
    logger.debug('Starting run function')

    with XLAMBuilder(dry=False) as builder:
        pass


if __name__ == '__main__':
    logger.setLevel('DEBUG')
    logger.debug('Running as main program')
    run()
