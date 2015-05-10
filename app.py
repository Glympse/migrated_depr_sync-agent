import tornado.web
import utilities

import api.v1.fs

class Manager:
    def __init__(self):
        self.env = utilities.Env()

manager = Manager()

app = tornado.web.Application([
    (r'/api/1/list', api.v1.fs.ListEndpoint, dict(manager=manager)),
    (r'/api/1/get', api.v1.fs.GetEndpoint, dict(manager=manager)),
    (r'/api/1/update', api.v1.fs.UpdateEndpoint, dict(manager=manager)),
])

if __name__ == '__main__':
    port = manager.env.get("API_PORT", "8080")
    server = utilities.TornadoServer(app, port)
    server.start()
