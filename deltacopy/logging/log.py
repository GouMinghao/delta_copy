from datetime import datetime

COLOR_ENCODE_DICT = {
    'white': '\033[0m',
    'black': '\033[030m',
    'red': '\033[031m',
    'green': '\033[032m',
    'yellow': '\033[033m',
    'blue': '\033[034m',
    'purple': '\033[035m',
    'cyan': '\033[036m',
}
END_ENCODE = '\033[0m'

DEFAULT_COLOR_DICT = {
    'debug': 'white',
    'info': 'white',
    'warning': 'yellow',
    'error': 'red'
}

default_time_format = "%Y-%m-%d, %H:%M:%S"

class Logger():
    def __init__(self, name, color_dict = DEFAULT_COLOR_DICT, time_format = default_time_format):
        self.color_dict = color_dict
        self.time_format = time_format
        self.name = name
    
    def _format_time(self):
        return datetime.now().strftime(self.time_format)

    def _format_name(self):
        return self.name

    def _format_log(self, logtype, content):
        return '{}[{}][{}][{}]: {}{}'.format(
            COLOR_ENCODE_DICT[self.color_dict[logtype]],
            self._format_time(),
            logtype,
            self._format_name(),
            content,
            END_ENCODE
        )

    def logdebug(self, debug):
        print(self._format_log(logtype = 'debug', content = debug))

    def loginfo(self, info):
        print(self._format_log(logtype = 'info', content = info))

    def logwarning(self, warning):
        print(self._format_log(logtype = 'warning', content = warning))

    def logerror(self, error):
        print(self._format_log(logtype = 'error', content = error))

