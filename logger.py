import copy, logging
import colorful
logger = None

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