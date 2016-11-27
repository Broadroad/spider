import stomp
import Queue


queue = Queue.Queue(1000)
class ActiveMqListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)
        queue.put(message)
        

