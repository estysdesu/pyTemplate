#!/usr/bin/env python3
# coding: utf-8

import os
import logging
import sys

import log_handlers


def main():
    log.info("app starting")


if __name__ == "__main__":
    log_dir = os.path.join(os.getcwd(), ".log")
    log = log_handlers.logger_setup(
        name="root", log_file_dir=log_dir, log_file_level=logging.DEBUG)
    )
    sys.exit(main())
