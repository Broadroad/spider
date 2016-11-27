"""
cofigure class, load conf
"""
import logging
import json

logger = logging.getLogger(__name__)

class Configure:
    confFile = ""

    def __init__(self, confFile = 'conf/scheduler.json'):
        BaseObject.__init__(self)
        self.confFile = confFile


    def load(self):
        try:
            with open(self.confFile, 'r') as f:
                conf = f.read() 
                self.confMap = json.loads(conf)
            return True
        except IOError as err:
            logger.error("Configure load failed, error info: " + str(err))
            return False

    @property
    def get(self):
        return self.confMap
            
