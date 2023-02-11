class Square:


    def __init__(self, x, y,color, edge):
        self.x = x
        self.y = y
        self.color = color
        self.edge = edge
    
    def create_figure(self, background):
        background.canvas[self.x:self.edge+self.x, self.y:self.edge+self.y] = self.color
        



class Rectangle:

    def __init__(self,x,y,width_rec,height_rec,color):
        self.x = x
        self.y = y
        self.width_rec = width_rec
        self.height_rec = height_rec
        self.color = color

    def create_figure(self, background):
        background.canvas[self.x:self.height_rec+self.x, self.y:self.width_rec+self.y] = self.color