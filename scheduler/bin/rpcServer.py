import pyjsonrpc

logger = logging.getLogger(__name__)

class RpcService:
    @pyjsonrpc.rpcmethod
    def crawl(self, url):
        print url


    def exec(self, cmd):
        print url

class RpcServer:
    def __init__(self, conf):
        self.server = pyjsonrpc.ThreadingHttpServer(
            server_address = ('localhost', 8080),
            RequestHandlerClass = RequestHandler
        )

        logger.info("rpc server init")
        self.server..serve_forever()
        

