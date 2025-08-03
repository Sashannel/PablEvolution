import NN
from graphics import *

class Creature():

    def __init__(self, window, max_x, max_y):

        self.x = 300
        self.y = 300
        self.health = 10
        self.food = 1
        self.is_Starving = False
        self.direction = 4 #0=STOP 1= LEFT 2= RIGHT 3= UP 4= DOWN
        self.velocity = 5
        self.id = 0
        self.window = window
        self.max_x = max_x
        self.max_y = max_y
        self.shape = Circle(Point(self.x, self.y), 5)
        self.shape.setFill('blue')
        self.shape.draw(window)
        print("Initial values:", self.x, self.y)

    def move(self, direction, x, y, velocity):

        if direction == 0: #STOP

            self.shape.move(0, 0)
            self.x = self.x
            self.y = self.y
            print("CELL STOPPED!")

        elif direction == 1: #LEFT

            if self.x - velocity  >= 0:
                self.shape.move(-velocity, 0)
                self.x = self.x - velocity
                self.y = self.y
                print("CELL GOING LEFT!")
            else:
                pass

        elif direction == 2: #RIGHT

            if self.x + velocity <= self.max_x:
                self.shape.move(velocity, 0)
                self.x = self.x + velocity
                self.y = self.y
                print("CELL GOING RIGHT!")
            else:
                pass

        elif direction == 3: #UP

            if self.y - velocity >= 0:
                self.shape.move(0, -velocity)
                self.x = self.x
                self.y = self.y - velocity
                print("CELL GOING UP!")
            else:
                pass

        elif direction == 4: #DOWN

            if self.y + velocity <= self.max_y:
                self.shape.move(0, velocity)
                self.x = self.x
                self.y = self.y + velocity
                print("CELL GOING DOWN!")
            else:
                pass

    def update(self):
        output = (NN.NN().brain([self.x, self.y, self.health, self.food, self.is_Starving, self.direction]))[0]
        self.direction = round(output) 
        self.move(self.direction, self.x, self.y, self.velocity)
        print("New values:", self.x, self.y)
        return "updated"
