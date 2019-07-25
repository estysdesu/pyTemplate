# coding: utf-8

import logging
import logging.handlers
import os
import time
from typing import *


class FileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, f_path, f_level=logging.DEBUG):
        super().__init__(f_path, when="D", interval=1, utc=True)
        self.setLevel(f_level)
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


def logger_setup(name: str = "root", **kwargs: Union[str, int]) -> logging.Logger:
    """
    Setup the logger.
    kwargs: stream_level, log_file_level, log_file_dir
    """
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)  # init w/ lowest level

    # stream logger
    if "stream_level" in kwargs.keys():
        stream_level = kwargs.get("stream_level")
    else:
        stream_level = logging.INFO
    sh = StreamHandler(s_level=stream_level)
    log.addHandler(sh)

    # file logger
    if "log_file_level" in kwargs.keys():
        log_file_level = kwargs.get("log_file_level")
    else:
        log_file_level = logging.DEBUG
    if "log_file_dir" in kwargs.keys():
        log_file_dir = kwargs.get("log_file_dir")
        os.makedirs(log_file_dir, exist_ok=True)  # type: ignore
        log_file_path = os.path.join(log_file_dir, log.name + ".log")  # type: ignore
        fh = FileHandler(log_file_path, f_level=log_file_level)
        log.addHandler(fh)

    return log
