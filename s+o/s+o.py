import os
import cv2

from o import ConfigParserFactory, ConfigLoader
        

class PathManager:
    """
    Manages the path and gets files.
    """
    def __init__(self, config):
        self.data_root = config['data']['root_dir']
        self.img_dir = os.path.join(self.data_root, "images")
        self.label_dir = os.path.join(self.data_root, "labels")
        self.mask_dir = os.path.join(self.data_root, "masks")
    
    def get_images(self):
        return os.listdir(self.img_dir)
    
    def get_labels(self):
        return os.listdir(self.label_dir)
    
    def get_masks(self):
        return os.listdir(self.mask_dir)
        

class DataLoader:
    """
    Load the image at a given index. 
    """
    def __init__(self, images, labels):
        self.imges = images
        self.labels = labels      

    def load_indexed_image(self, img_dir, index):
        image_path = os.path.join(img_dir, self.imges[index])
        return cv2.imread(image_path)

    
if __name__ == "__main__":
    path = "./config.json"
    parser = ConfigParserFactory.get_parser(path)
    config_loader = ConfigLoader(parser, path)
    config = config_loader.load()
    
    data_path = PathManager(config=config)
    images = data_path.get_images()
    labels = data_path.get_labels()
    masks = data_path.get_masks()
    
    loader = DataLoader(images, labels)
    im = loader.load_indexed_image(data_path.img_dir, 0)
    if im is not None:
        print(f"The image is loaded. The size is: {im.shape}")
    else:
        print("Could not load the image.")
        