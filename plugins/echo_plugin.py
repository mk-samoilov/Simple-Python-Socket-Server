from plugins import BasePlugin

class Plugin(BasePlugin):
    def server_started(self):
        pass

    def process_client_pkg(self, data):
        if data.startswith("ECHO "):
            return data[5:]

        return None
