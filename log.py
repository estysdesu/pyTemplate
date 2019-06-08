import logging, os, time

# create .log file directory and file
logDir = os.path.join(os.getcwd(), ".log")
os.makedirs(logDir, exist_ok=True)
logFile = os.path.join(logDir, "ECGpy.log")

# create logger
Logger = logging.getLogger("ECGpy") # app logger
Logger.setLevel(logging.DEBUG) # includes all output

fh = logging.FileHandler(logFile) # file handler 
fh.setLevel(logging.DEBUG) # logs debug and up
logFmtFile =  logging.Formatter(fmt="%(asctime)s: %(filename)s:%(lineno)s - %(levelname)s: %(funcName)s: %(message)s", datefmt="%y/%m/%d %H:%M:%S")
logFmtFile.converter = time.gmtime # change time to utc
fh.setFormatter(logFmtFile)
Logger.addHandler(fh)

ch = logging.StreamHandler() # console logger
ch.setLevel(logging.INFO) # logs info and up
logFmtCon =  logging.Formatter(fmt="%(filename)s:%(lineno)s - %(levelname)s: %(funcName)s: %(message)s")
ch.setFormatter(logFmtCon)
Logger.addHandler(ch)
