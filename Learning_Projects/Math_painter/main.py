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
from canvas import Canvas
    
canvas_height = int(input("Give the height of the canvas: "))
canvas_width = int(input("Give the witdth of the canvas: "))
canv = Canvas(canvas_height,canvas_width)
chosen_color = str(input("Choose color of the canvas (black/white): "))
matrix = canv.create_canvas(chosen_color)





