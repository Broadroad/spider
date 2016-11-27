import logging

class BaseObject:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG, format = '[%(asctime)s] %(levelname)s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

