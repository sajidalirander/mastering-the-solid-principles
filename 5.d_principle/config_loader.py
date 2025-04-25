from config_reader import ConfigReader

class ConfigLoader:
    def __init__(self, reader: ConfigReader, path: str):
        self.reader = reader
        self.path = path

    def load_config(self) -> dict:
        return self.reader.load(self.path)
