## Open/Closed Principle (OCP)
> Open for extension but closed for modification -- able to add new features without changing old code.

### _without OCP_
```python 
class ConfigLoader:
    def load(self, path):
        with open(path, "r") as file:
            return yaml.safe_load(file)
```
It does not support other file extensions. 


### _with OCP_
```python
class ConfigLoader:
    def __init__(self, parser: ConfigParser, path: str):
        self.parser = parser
        self.path = path

    def load(self):
        return self.parser.load(self.path)
```

An abstract interface:
```python 
from abc import ABC, abstractmethod

class ConfigParser(ABC):
    @abstractmethod
    def load(self, path: str) -> dict:
        pass
```

Implementing YAML loader:
```python 
import yaml
from config_parser import ConfigParser

class YamlConfigParser(ConfigParser):
    def load(self, path):
        with open(path, "r") as file:
            return yaml.safe_load(file)
```

Implementing JSON support:
```python
import json
from config_parser import ConfigParser

class JsonConfigParser(ConfigParser):
    def load(self, path):
        with open(path, "r") as file:
            return json.load(file)
```