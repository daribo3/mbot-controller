import logging


class LogFormatter(logging.Formatter):
    DEBUG_FMT = "%(asctime)s %(module)-15s %(levelname)-7s (%(name)s:%(funcName)s:%(lineno)d) %(message)s"
    ERROR_FMT = "%(asctime)s %(module)-15s %(levelname)-7s %(message)s"
    DEFAULT_FMT = "%(asctime)s %(module)-15s %(levelname)-7s %(message)s"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._debug_fmt = logging.Formatter(self.DEBUG_FMT)
        self._error_fmt = logging.Formatter(self.ERROR_FMT)
        self._default_fmt = logging.Formatter(self.DEFAULT_FMT)

    def format(self, record) -> str:
        match (record.levelno):
            case logging.DEBUG:
                log_message = self._debug_fmt.format(record)
            case logging.ERROR:
                log_message = self._error_fmt.format(record)
            case _:
                log_message = self._default_fmt.format(record)
        return log_message


def setup_logging(log_level: str = "info", config_file: str = None):
    if config_file:
        logging.config.fileConfig(config_file)

    root = logging.getLogger("mbotcontroller")
    fmt = LogFormatter()

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)

    root.handlers = []
    root.addHandler(stream_handler)
    root.setLevel(log_level.upper())
