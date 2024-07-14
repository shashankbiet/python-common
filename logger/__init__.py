from .levels import LogLevel
from .console_logger import ConsoleLogger

defaultLogger = None
defaultLogLevel = LogLevel.INFO

class AppLogger:
    def __init__(self):
        self.logger = ConsoleLogger()
        self.logLevel = defaultLogLevel

def init_default_logger(logType, logLevel):
    global defaultLogger
    logger = get_logger(logType)
    defaultLogger = AppLogger()
    defaultLogger.logger = logger
    defaultLogger.logLevel = logLevel

def get_logger(logType):
    if logType == 'console':
        return ConsoleLogger()
    return ConsoleLogger()

def debug(message, *keyValues):
    if defaultLogger and defaultLogger.logLevel <= LogLevel.DEBUG:
        defaultLogger.logger.debug(message, *keyValues)

def info(message, *keyValues):
    if defaultLogger and defaultLogger.logLevel <= LogLevel.INFO:
        defaultLogger.logger.info(message, *keyValues)

def warn(message, *keyValues):
    if defaultLogger and defaultLogger.logLevel <= LogLevel.WARN:
        defaultLogger.logger.warn(message, *keyValues)

def error(message, *keyValues):
    if defaultLogger and defaultLogger.logLevel <= LogLevel.ERROR:
        defaultLogger.logger.error(message, *keyValues)

# Initialize the default logger
defaultLogger = AppLogger()
