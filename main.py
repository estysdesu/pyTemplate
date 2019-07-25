#!/usr/bin/env python3
# coding: utf-8

import os
import sys

import log_handlers


def main():
    log.info("app starting")
    return


if __name__ == "__main__":
    log_dir = os.getcwd()
    log = log_handlers.logger_setup(name="root", log_dir=log_dir)
    sys.exit(main())
