# coding: utf-8

import logging
import time
import typing
import logging.handlers


class FileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, fPath, fLevel=logging.DEBUG):
        super().__init__(fPath, when="D", interval=1, utc=True)
        self.setLevel = fLevel
        fmt = logging.Formatter(
            fmt="%(asctime)s - %(levelname)-8s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s",
            datefmt="%y%m%d %H:%M:%S",
        )
        fmt.converter = time.gmtime
        self.setFormatter(fmt)


class StreamHandler(logging.StreamHandler):
    def __init__(self, sLevel=logging.INFO):
        super().__init__()
        self.setLevel(sLevel)
        fmt = logging.Formatter(
            fmt="%(levelname)-8s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s"
        )
        self.setFormatter(fmt)


def logger_setup(log_dir: Optional[str] = None) -> logging.Logger:
    log = logging.getLogger("root")
    log.setLevel(logging.DEBUG)

    stream_level = logging.DEBUG
    sh = log_handlers.StreamHandler(sLevel=stream_level)
    log.addHandler(sh)

    if log_dir is not None:
        file_level = logging.INFO
        os.makedirs(logDir, exist_ok=True)
        logFile = os.path.join(logDir, log.name + ".log")
        fh = log_handlers.FileHandler(logFile, file_level)
        log.addHandler(fh)

    return log
