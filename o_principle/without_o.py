import yaml


class ConfigLoader:
    """
    Loading YAML config file.
    It cannot support other file extensions.
    """
    def __init__(self, config_path):
        self.config_path = config_path

    def load(self):
        with open(self.config_path, "r") as file:
            return yaml.safe_load(file)
  
        
if __name__ == "__main__":
    path = "./config.yaml"
    config_loader = ConfigLoader(config_path=path)
    config = config_loader.load()
    if config is not None:
        print("Loaded the config successfully.")
    else:
        print("Could not load.")