# file_handling.py
from abc import ABC, abstractmethod

class YamlReader(ABC):
    @abstractmethod
    def read_yaml(self, path):
        pass

class JsonReader(ABC):
    @abstractmethod
    def read_json(self, path):
        pass
