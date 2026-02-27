import random
import os

class SwiperLogic:
    def __init__(self, win_chance=0.20):
        self.win_chance = win_chance

    def get_next_image_type(self):
        """Randomly determines if the next image is a 'right swipe' (dog) or 'left swipe' (cat)."""
        if random.random() < self.win_chance:
            return "dogs"
        return "cats"

    def get_random_image(self, img_type):
        """Picks a random image file"""
        folder_path = os.path.join('static', 'images', img_type)
        images = os.listdir(folder_path)
        return random.choice(images)