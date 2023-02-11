from PIL import Image
import numpy as np

class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def create_canvas(self):
        self.canvas = np.zeros((self.height,self.width,3), dtype=np.uint8)
        self.canvas[:] = self.color
        

    def generate_img(self, name_of_image):
        final_canvas = Image.fromarray(self.canvas, "RGB")
        final_canvas.save(name_of_image)