import json
import tornado
import tornado.web

"""
Implements JSON encoding and JSONP on top of tornado.web.RequestHandler.
"""
class JsonRequestHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self, **args):
        self.process(args)

    @tornado.web.asynchronous
    def post(self, **args):
        self.process(args)

    @tornado.web.asynchronous
    def options(self, **args):
        self.set_header("Access-Control-Allow-Methods",
            self.request.headers.get("Access-Control-Request-Methods", default="*"))
        self.set_header("Access-Control-Allow-Headers",
            self.request.headers.get("Access-Control-Request-Headers", default="*"))
        self.set_header("Content-Type", "text/html; charset=utf-8")
        self.finish()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def process(self, args):
        # Handle the call
        try:
            # Handle authentication
            self.handle_auth()

            # Propagate to business logic
            response = self.handle(args)
            if isinstance(response, dict) or isinstance(response, list):
                output = json.dumps({ "result": "ok", "body": response })
                self.set_header("Content-Type", "application/json")
            else:
                output = response
                self.set_header("Content-Type", "text/plain")
        except NameError as e:
            output = '{ "result": "failure", "error": {0} }'.format( e.message )
        except Exception as e:
            output = '{ "result": "failure" }'

        # Send the response.
        self.write(output)
        self.finish()

    def handle_auth(self):
        pass

    def handle(self, args):
        pass

"""
Provides skeleton of authenticated endpoint.
"""
class ApiHandler(JsonRequestHandler):

    def initialize(self, manager):
        self.manager = manager

"""
Provided to prevent dyno from sleeping.
"""
class AwakeEndpoint(JsonRequestHandler):

    def handle(self, args):
        return {}
