import logging
import stomp
import gevent
import Queue
from gevent import GreenletExit
from gevent.pool import Group
import request
from request import KirinRequest
import redis
from mqHandler import ActiveMqListener, queue

kirin_runner = None
logger = logging.getLogger(__name__)
ch = logging.StreamHandler()  
ch.setLevel(logging.INFO)
fh = logging.FileHandler('/tmp/test.log')  
logger.addHandler(ch)
logger.addHandler(fh)

class KirinRunner(object):
    def __init__(self):
        self.kirins = Group()
        #self.urls = ['http://www.baidu.com', 'www.sina.com.cn']
        #self.hatch_greenlet = None
        #self.r = redis.StrictRedis(host='127.0.0.1', port=6379)
        self.conn = stomp.Connection([('127.0.0.1', 61613)])
        self.conn.set_listener('', ActiveMqListener())
        self.conn.start()
        self.conn.connect('admin', 'admin', wait=True)
        self.conn.subscribe('/queue/urls', 123)
 
    def start_hatching(self):
        logger.info('start_hatching')
        self.hatch_greenlet = gevent.spawn(self.spawn_kirin())

    def spawn_kirin(self):

        def hatch():
            while True:
                """
                get url from queue
                """
                url = self.get_url()
                def start_kirin(_):
                    try:
                        response = KirinRequest(url, 'GET').request()
                        print response.status_code
                        logger.info("crawl the url" + url)
                    except GreenletExit:
                        pass

                new_kirin = self.kirins.spawn(start_kirin, url)
                gevent.sleep(1)
        hatch()
        self.kirins.join()
        logger.info("All the urls are crawled")

    def get_url(self):
        return self.build_url(queue.get()) 

    def build_url(self, url):
        try:
            return "http://" + url
        except:
            logger.error("the redis queue is emtpy")
            return "http://www.baidu.com"

