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
from background import Canvas
from figures import Square, Rectangle

width_of_canv = int(input("What is the width of the canvas ?:"))
height_of_canv = int(input("What is the height of the canvas ?:"))
R = int(input("Give value of the RED (0-255):"))
G = int(input("Give value of the GREEN (0-255):"))
B = int(input("Give value of the BLUE (0-255):"))
canv = Canvas(height_of_canv,width_of_canv, (R,G,B))
canv_table = canv.create_canvas()
canv.generate_img("Canvas.png")

while True:

    answer = int((input("Select what you want to do(number of choice):\n 1.Draw square\n 2.Draw rectangle\n 3.Exit\n")))

    if answer == 1:
        start_point_x = int(input("Give X value: "))
        start_point_y = int(input("Give Y value: "))
        len_of_edge = int(input("Give the length of the edge: "))
        R = int(input("Give value of the RED (0-255):"))
        G = int(input("Give value of the GREEN (0-255):"))
        B = int(input("Give value of the BLUE (0-255):"))
        sq = Square(start_point_x,start_point_y,(R,G,B),len_of_edge)
        sq.create_figure(canv)
        canv.generate_img("Canvas.png")

    if answer == 2:
        start_point_x = int(input("Give X value: "))
        start_point_y = int(input("Give Y value: "))
        len_of_width = int(input("Give the length of the first edge: "))
        len_of_height = int(input("Give the length of the second edge: "))
        R = int(input("Give value of the RED (0-255):"))
        G = int(input("Give value of the GREEN (0-255):"))
        B = int(input("Give value of the BLUE (0-255):"))
        rec = Rectangle(start_point_x,start_point_x,len_of_width,len_of_height,(R,G,B))
        rec.create_figure(canv)
        canv.generate_img("Canvas.png")

    if answer == 3:
        print("Thanks for drawing :)")
        canv.generate_img("Canvas.png")
        break
