import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def create_canvas(self, background_color):
        canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        if background_color == "black":
            canvas[:] = [0,0,0]
        elif background_color == "white":
            canvas[:] = [255,255,255]
        else:
            print("There are only two options black and white for now")
            print("The color has been selected by program as a white")
            canvas[:] = [255,255,255]

        final_canvas = Image.fromarray(canvas, "RGB")
        final_canvas.save("Canvas.png")