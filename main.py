#!/usr/bin/env python3
# coding: utf-8

import sys, logging

def main():
    log.info("app starting")
    return
    
if __name__ == "__main__":
    log = logging.getLogger("root")
    log.setLevel(logging.DEBUG)
    sh = logHandlers.StreamHandler()
    log.addHandler(sh)
    logDir = os.path.join( os.getcwd(), "<.appName>")
    logFile = os.path.join(logDir, "root.log")
    os.makedirs(logDir, exist_ok=True)
    fh = logHandlers.FileHandler(logFile)
    log.addHandler(fh)
   
    sys.exit(main())
