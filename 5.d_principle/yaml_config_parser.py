import yaml
from config_reader import ConfigReader

class YamlConfigParser(ConfigReader):
    def load(self, path: str) -> dict:
        with open(path, "r") as file:
            return yaml.safe_load(file)
