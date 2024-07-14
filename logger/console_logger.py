import logging

class ConsoleLogger:
    def __init__(self):
        self.logger = logging.getLogger('console_logger')
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.DEBUG)

    def debug(self, message, *args):
        self.logger.debug(message, *args)

    def info(self, message, *args):
        self.logger.info(message, *args)

    def warn(self, message, *args):
        self.logger.warning(message, *args)

    def error(self, message, *args):
        self.logger.error(message, *args)
