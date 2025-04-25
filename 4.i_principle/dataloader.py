import os
import cv2


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
