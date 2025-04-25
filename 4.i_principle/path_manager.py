import os


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
    