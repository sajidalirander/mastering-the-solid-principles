import os
import cv2
import yaml


class DataLoader:
    """
    It is doing three tasks:
    1. reading config.yaml
    2. image and label paths 
    3. load image at index
    """
    def __init__(self):
        with open("./config.yaml", "r") as file:
            cfg = yaml.safe_load(file)

        self.data_root = cfg['data']['root_dir']
        self.img_dir = os.path.join(self.data_root, "images")
        self.label_dir = os.path.join(self.data_root, "labels")
        
        self.images = os.listdir(self.img_dir)
        self.labels = os.listdir(self.label_dir)

    def load_indexed_image(self, index):
        image_path = os.path.join(self.img_dir, self.images[index])
        
        return cv2.imread(image_path)
    
if __name__ == "__main__":
    index = 0
    loader = DataLoader()
    im = loader.load_indexed_image(index)
    if im is not None:
        print("The image is loaded.")
    else:
        print("Could not load the image.")