# coding: utf-8

import logging
import logging.handlers
import os
import time
from typing import *


class FileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, f_path, f_level=logging.DEBUG):
        super().__init__(f_path, when="D", interval=1, utc=True)
        self.setLevel = f_level
        fmt = logging.Formatter(
            fmt="%(asctime)s - %(levelname)-8s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s",
            datefmt="%y%m%d %H:%M:%S",
        )
        fmt.converter = time.gmtime
        self.setFormatter(fmt)


class StreamHandler(logging.StreamHandler):
    def __init__(self, s_level=logging.INFO):
        super().__init__()
        self.setLevel(s_level)
        fmt = logging.Formatter(
            fmt="%(levelname)-8s - %(filename)s:%(funcName)s:%(lineno)s - %(message)s"
        )
        self.setFormatter(fmt)


def logger_setup(name: str = "root", log_dir: Optional[str] = None) -> logging.Logger:
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    stream_level = logging.DEBUG
    sh = StreamHandler(s_level=stream_level)
    log.addHandler(sh)

    if log_dir is not None:
        file_level = logging.INFO
        os.makedirs(log_dir, exist_ok=True)
        logFile = os.path.join(log_dir, log.name + ".log")
        fh = FileHandler(logFile, f_level=file_level)
        log.addHandler(fh)

    return log
