###############################################################
#     Program rysuje na określonej przez użytkownika          # 
#     powierzchni dwa rodzaje figur geometrycznych,           #
#     prostokąty i kwadraty. Użytkownik jest w stanie         #
#     określić parametry figur zaczynając od podania          #
#     współrzędnych lewego górnego wierzchołka, oraz          #
#     długości dwóch boków - w przypadku prostokąta,          #
#     oraz jednego boku - w przypadku kwadratu podaje         # 
#     także kolor wypełnienia. Dodatkowo użytkownik           #
#     określa kolor tła. Sam decyduje kiedy kończy            #
#     rysowanie figur.                                        #   
###############################################################
import numpy as np
from PIL import Image

class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def create_canvas(self, background_color):
        canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        try:
            if background_color == "black":
                canvas[:] = [0,0,0]
            elif background_color == "white":
                canvas[:] = [255,255,255]
        except:
            print("There are only two options black and white for now")
            print("The color has been selected by program")
            canvas[:] = [255,255,255]
            return canvas
        final_canvas = Image.fromarray(canvas, "RGB")
        final_canvas.save("Canvas.png")

        
canvas_height = int(input("Give the height of the canvas: "))
canvas_width = int(input("Give the witdth of the canvas: "))
canv = Canvas(canvas_height,canvas_width)
chosen_color = str(input("Choose color of the canvas (black/white): "))
matrix = canv.create_canvas(chosen_color)





