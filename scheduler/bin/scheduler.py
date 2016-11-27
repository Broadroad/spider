from taskLoader import TaskLoader 
from configure import Configure
import logging

logger = logging.getLogger(__name__)

class Scheduler:
    def __init__(self):
        self.taskLoader = TaskLoader("data/urls.txt")
        #self.conf = Configure()

    def init(self):
       # if self.conf.load() == False:
       #     self.logger.fatal("configure load failed")
       #     return False

        logger.info("init ok")

        self.taskLoader.load() 

        
