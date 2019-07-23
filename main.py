#!/usr/bin/env python3
# coding: utf-8

import sys

import logHandlers


def main():
    log.info("app starting")
    return


if __name__ == "__main__":
    log_dir = os.getcwd()
    log = logHandlers.logger_setup(log_dir)
    sys.exit(main())
