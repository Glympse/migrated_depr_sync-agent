import os
import signal
import configparser
import xml.etree.ElementTree
import json
import tornado.httpserver
import tornado.ioloop

class File:
    @staticmethod
    def read(path):
        file = open(path, "r")
        text = file.read()
        file.close()
        return text

    @staticmethod
    def write(path, text):
        file = open(path, "w")
        file.write(text)
        file.close()

    @staticmethod
    def read_xml(path):
        return xml.etree.ElementTree.XML(File.read(path))

    @staticmethod
    def read_json(path):
        return json.loads(File.read(path))

    @staticmethod
    def write_json(path, obj):
        File.write(path, json.dumps(obj, indent=2, separators=(',', ': ')))

"""
Handles environment variables in target-specific way
"""
class Env:
    def __init__(self):
        if os.path.exists(".env"):
            self.config = configparser.ConfigParser()
            self.config.read('.env')
        else:
            self.config = None

    def get(self, name, default=None):
        if self.config:
            return self.config.get("DEFAULT", name, fallback=default)
        else:
            return os.environ.get(name, default)

class TornadoServer:
    def __init__(self, app, port):
        self.app = app
        self.port = int(os.environ.get("PORT", port))

    def handler(self, signum, frame):
        tornado.ioloop.IOLoop.instance().add_callback(self.shutdown)

    def start(self):
        signal.signal(signal.SIGTERM, self.handler)
        signal.signal(signal.SIGINT, self.handler)

        self.server = tornado.httpserver.HTTPServer(self.app)
        self.server.listen(self.port)
        tornado.ioloop.IOLoop.instance().start()

    def shutdown(self):
        self.server.stop()
        tornado.ioloop.IOLoop.instance().stop()
