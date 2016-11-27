import stomp
from stomp import *

class TaskLoader():

    def __init__(self, urlFile):
        self.urlFile = urlFile 
        self.conn = stomp.Connection([('127.0.0.1', 61613)]) 
        self.conn.start()
        self.conn.connect('admin', 'admin', wait=True)


    def load(self):
        reader = self.byLineReader()
        line = reader.next()
        while line:
            self.processLine(line)
            line = reader.next()


    def byLineReader(self):
        f = open(self.urlFile)
        line = f.readline()
        while line:
            yield line
            line = f.readline()
        f.close()
        yield None
        

    def processLine(self, line):
        line = line.strip()
        self.conn.send('/queue/urls', line, header={'AMQ_SCHEDULED_PERIOD': 3000})


