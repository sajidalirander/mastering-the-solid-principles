from abc import ABC, abstractmethod

class ConfigReader(ABC):
    @abstractmethod
    def load(self, path: str) -> dict:
        pass
