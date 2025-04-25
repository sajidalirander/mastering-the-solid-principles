# dataloader.py
from path_manager import DataPathProvider
import os
import cv2

class DataLoader:
    def __init__(self, path_provider: DataPathProvider):
        self.path_provider = path_provider

    def load_indexed_image(self, index: int):
        images = self.path_provider.get_images()
        if index < 0 or index >= len(images):
            return None
        
        img_path = os.path.join(self.path_provider.img_dir, images[index])
        img = cv2.imread(img_path)
        return images[index]
