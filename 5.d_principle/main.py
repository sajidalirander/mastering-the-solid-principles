from config_loader import ConfigLoader
from config_parser_factory import get_parser

from path_manager import PathManager
from dataloader import DataLoader


def create_data_loader(path: str) -> DataLoader:
    parser = get_parser(path)
    config_loader = ConfigLoader(parser, path)
    config = config_loader.load_config()
    
    paths = PathManager(config=config)
    
    return DataLoader(paths)


if __name__ == "__main__":
    config_file_path = "./config.json"
    loader = create_data_loader(config_file_path)
    
    im = loader.load_indexed_image(index=7)
    
    print(f"Loaded image is: {im}")