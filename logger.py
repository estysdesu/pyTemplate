import logging, os, time, datetime

class NewLogger():
    def __init__(self, logName, level, fileDir=None, fileLevel=None):
        self.logName = logName
        self.level = level
        self.fileDir = fileDir
        self.fileLevel = fileLevel

        self.logger = self.new()
        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error


    def new(self):
        logger = logging.getLogger(self.logName)
        # level = self.check_level(self.level)
        # logger.setLevel(level)

        consoleHandler = self.get_ch(self.level)
        logger.addHandler(consoleHandler)

        fh = False
        if self.fileDir is not None:
            fh = True
        if self.fileLevel is not None:
            fh = True
        if fh:
            fileHandler = self.get_fh(self.logName, self.fileDir, self.fileLevel)
            logger.addHandler(fileHandler)

        return logger

    def get_ch(self, levelConsole):
        ch = logging.StreamHandler()
        level = self.check_level(levelConsole)
        ch.setLevel(level)
        fmt =  logging.Formatter(fmt="%(filename)s:%(lineno)s - %(levelname)s: %(funcName)s: %(message)s")
        ch.setFormatter(fmt)
        return ch
    
    def get_fh(self, logName, outDir, levelFile):
        if outDir is None:
            outDir = os.getcwd()
        if levelFile is None:
            levelFile = self.level

        outDir = os.path.abspath(outDir)
        logDir = os.path.join(outDir, "."+logName)
        os.makedirs(logDir, exist_ok=True)
        date = datetime.datetime.utcnow().strftime("%y%m%d")
        logFile = os.path.join(logDir, date+".log")

        fh = logging.FileHandler(logFile)
        level = self.check_level(levelFile)
        fh.setLevel(level)
        fmt = logging.Formatter(fmt="%(asctime)s: %(filename)s:%(lineno)s - %(levelname)s: %(funcName)s: %(message)s", datefmt="%y/%m/%d %H:%M:%S")
        fmt.converter = time.gmtime
        fh.setFormatter(fmt)
        return fh

    def check_level(self, level):
        pkgLevels = [logging.DEBUG, logging.WARNING, logging.INFO, logging.ERROR, logging.CRITICAL]
        level = level.lower()
        if level == "debug":
            logLevel= logging.DEBUG
        elif level == "info":
            logLevel = logging.INFO
        elif level == "warning":
            logLevel = logging.WARNING
        elif level == "error":
            logLevel = logging.ERROR
        elif level in pkgLevels:
            logLevel = level
        else:
            raise Exception("levelOut is not configured correctly")
        return logLevel

if __name__ != "__main__":
    import logger
    Log = logger.NewLogger("myapp", "warning", fileDir=".", fileLevel="debug")

