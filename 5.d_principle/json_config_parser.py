import json
from config_reader import ConfigReader

class JsonConfigParser(ConfigReader):
    def load(self, path: str) -> dict:
        with open(path, "r") as file:
            return json.load(file)
