import os
from yaml_config_parser import YamlConfigParser
from json_config_parser import JsonConfigParser
from config_reader import ConfigReader

def get_parser(path: str) -> ConfigReader:
    ext = os.path.splitext(path)[-1].lower()
    if ext in [".yaml", ".yml"]:
        return YamlConfigParser()
    elif ext == ".json":
        return JsonConfigParser()
    else:
        raise ValueError(f"Unsupported config file format: {ext}")
