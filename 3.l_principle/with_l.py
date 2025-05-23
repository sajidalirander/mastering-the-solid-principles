import os
import json
import yaml
from abc import ABC, abstractmethod

    
class ConfigParser(ABC):
    @abstractmethod
    def load(self, path):
        pass
    

class ConfigLoader:
    def __init__(self, parser, path):
        self.parser = parser
        self.path = path

    def load(self):
        return self.parser.load(self.path)


class YamlConfigParser(ConfigParser):
    def load(self, path):
        with open(path, "r") as file:
            return yaml.safe_load(file)        


class JsonConfigParser(ConfigParser):
    def load(self, path):
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
            raise ValueError(f"Unsupported extension: {ext}")


if __name__ == "__main__":
    path = "./config.json"
    parser = ConfigParserFactory.get_parser(path)
    config_loader = ConfigLoader(parser, path)
    config = config_loader.load()
    if config is not None:
        print("Loaded the config successfully.")
    else:
        print("Could not load.")
        
