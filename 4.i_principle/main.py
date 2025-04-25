from configuration import ConfigParserFactory, ConfigLoader
from path_manager import PathManager
from dataloader import DataLoader


if __name__ == "__main__":
    path = "./config.yaml"
    parser = ConfigParserFactory.get_parser(path)
    config_loader = ConfigLoader(parser, path)
    config = config_loader.read()
    
    data_path = PathManager(config=config)
    images = data_path.get_images()
    labels = data_path.get_labels()
    masks = data_path.get_masks()
    
    loader = DataLoader(images, labels)
    im = loader.load_indexed_image(data_path.img_dir, 1)
    if im is not None:
        print(f"The image is loaded. The size is: {im.shape}")
    else:
        print("Could not load the image.")
        