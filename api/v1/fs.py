import os
import api.rest

class ListEndpoint(api.rest.ApiHandler):
    def handle(self, args):
        folder = self.manager.env.get("SYNC_FOLDER")
        files = ListEndpoint.get_files(folder)
        return files

    @staticmethod
    def get_files(folder):
        files = []
        for filename in os.listdir(folder):
            files.append({ "name": filename })
        return files

class GetEndpoint(api.rest.ApiHandler):
    def handle(self, args):
        folder = self.manager.env.get("SYNC_FOLDER")
        name = self.get_argument("name")
        filename = folder + "/" + name
        file = open(filename, "r")
        data = file.read()
        file.close()
        return data

class UpdateEndpoint(api.rest.ApiHandler):
    def handle(self, args):
        folder = self.manager.env.get("SYNC_FOLDER")
        name = self.get_argument("name")
        data = self.request.body
        filename = folder + "/" + name
        file = open(filename, "wb")
        file.write(data)
        file.close()
        return {}
