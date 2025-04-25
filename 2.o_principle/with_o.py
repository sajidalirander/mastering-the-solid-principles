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


if __name__ == "__main__":
    path = "./config.json"
    config_loader = ConfigLoader(JsonConfigParser(), path)
    
    # # or
    # path = "./config.yaml"
    # config_loader = ConfigLoader(YamlConfigParser(), path)
    
    config = config_loader.load()
    print(config)
    if config is not None:
        print("Loaded the config successfully.")
    else:
        print("Could not load.")
        
