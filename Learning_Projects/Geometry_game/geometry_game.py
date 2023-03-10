###########################################
# Sprawdza czy dane koordynaty w formacie #
# (x,y), znajdują się w wyznaczonym polu  #
# Aplikacja ma na celu przećwiczenie      #
#wykorzystywania klas                     #
#                                         #
###########################################
#Stworzenie klasy punktu

import turtle as t
from random import randint as r

class Point:
    
    #Określenie parametrów punktu
    def __init__(self,x,y):
        self.x = x
        self.y = y

    
    #Sprawdzenie czy znajduje się w polu zainteresowania zbudowanie metody

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x<self.x<rectangle.point2.x \
            and rectangle.point1.y<self.y<rectangle.point2.y:
            return True
        else:
            return False
    
    #Obliczanie odległości pomiędzy dwoma punktami

    def distance_from_points(self, point):
        return ((self.x-point.x)**2+(self.y-point.y)**2)**0.5

# Stworzenie klasy pola

class Rectangle:

    def __init__(self,point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x)*(self.point2.y-self.point1.y)
    
class GuiRectangle(Rectangle): # Owa klasa posiada atrybuty klasy rectangle, dodatkowo dodaje nową funkcjonalność bez ingerencji w działające klasy

    def draw(self, canvas):

        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

class GuiPoint(Point):

    def add_point(self, pointmark):

        pointmark.penup()
        pointmark.goto(self.x, self.y)
        pointmark.pendown()
        pointmark.dot("red")





rectangle = GuiRectangle(
    Point(r(0,400), r(0,400)),
    Point(r(10,400), r(10,400)))

print(f"Rectangle Coordinates: ({rectangle.point1.x}, {rectangle.point1.y}) and ({rectangle.point2.x}, {rectangle.point2.y}) ")

user_point = GuiPoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

print(f"Answer: {user_point.falls_in_rectangle(rectangle)}")
print(f"Area of rectangle: {rectangle.area()}")
print(f"Your area was off by: {rectangle.area() - user_area}")

myturtle = t.Turtle()
userpoint = t.Turtle()
rectangle.draw(canvas = myturtle)
user_point.add_point(userpoint)
t.done()