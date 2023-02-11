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
from PIL import Image
import numpy as np

class Canvas:

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def create_canvas(self):
        self.canvas = np.zeros((self.height,self.width,3), dtype=np.uint8)
        return self.canvas

    def select_color(self):
        
        if self.color == "black":
            self.canvas[:] = [0,0,0]
        elif self.color == "white":
            self.canvas[:] = [255,255,255]
        else:
            print("There are only two options black and white for now")
            print("The color has been selected by program as a white")
            self.canvas[:] = [255,255,255]
        return self.canvas

    def generate_img(self, final_art):
        final_canvas = Image.fromarray(final_art, "RGB")
        final_canvas.save("Canvas.png")



class Square:

    def __init__(self, x, y,color, edge):
        self.x = x
        self.y = y
        self.color = color
        self.edge = edge
    
    def create_figure(self, background):
        self.square = background.canvas[self.x:self.edge, self.y:self.edge] = [255,0,0]
        
        return self.square

        

    def select_square_color(self):
        pass


class Rectangle:
    def __init__(self) -> None:
        pass


canv = Canvas(10,10, "white")
canv_table = canv.create_canvas()
color = canv.select_color()
squaree = Square(1,1,"any",3)
sq = squaree.create_figure(color)
print(sq)
