import os
import json
import yaml

from file_handling import YamlReader, JsonReader


class ConfigLoader:
    def __init__(self, parser, path):
        self.parser = parser
        self.path = path

    def read(self):
        if isinstance(self.parser, YamlReader):
            return self.parser.read_yaml(self.path)
        elif isinstance(self.parser, JsonReader):
            return self.parser.read_json(self.path)
        else:
            raise ValueError("Unsupported parser type.")


class YamlConfigParser(YamlReader):
    def read_yaml(self, path):
        with open(path, "r") as file:
            return yaml.safe_load(file)        


class JsonConfigParser(JsonReader):
    def read_json(self, path):
        with open(path, "r") as file:
            return json.load(file)


class ConfigParserFactory:
    @staticmethod
    def get_parser(path):
        ext = os.path.splitext(path)[-1].lower()
        
        if ext in [".yaml", ".yml"]:
            return YamlConfigParser()
        elif ext == ".json":
            return JsonConfigParser()
        else:
            raise ValueError(f"Unsupported config file extension: {ext}")
