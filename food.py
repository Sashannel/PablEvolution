from graphics import *
import random

class Food():

    def __init__(self, window, max_x, max_y):

        print("New food created")
        self.x = random.randint(0, max_x)
        self.y = random.randint(0, max_y)
        self.is_Dead = False
        self.window = window
        self.max_x = max_x
        self.max_y = max_y
        self.shape = Circle(Point(self.x, self.y), 5)
        self.shape.setFill('red')
        self.shape.draw(window)

    def update(self):

        if self.is_Dead:

            self.shape.undraw()

            return "death"
