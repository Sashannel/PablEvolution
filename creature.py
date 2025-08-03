import NN
from graphics import *
import random
import food

class Creature():

    def __init__(self, window, max_x, max_y):

        self.x = random.randint(0, max_x)
        self.y = random.randint(0, max_y)
        self.health = 10
        self.food = 300
        self.is_Starving = False
        self.direction = 4 #0=STOP 1= LEFT 2= RIGHT 3= UP 4= DOWN
        self.velocity = 5
        self.is_Dead = False
        self.id = 0
        self.window = window
        self.max_x = max_x
        self.max_y = max_y
        self.shape = Circle(Point(self.x, self.y), 5)
        if self.is_Dead == False:
            self.shape.setFill('blue')
        else:
            self.shape.setFill('black')
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
        if self.food == 0:
            self.is_Starving = True
        if self.food < 0:
            self.food = 0
            self.is_Starving = True
        if self.food > 0:
            self.is_Starving = False
            self.food -= 1
        if self.is_Starving == True:
            self.health -= 1

        if self.health <= 0:
            self.is_Dead = True
            self.shape.undraw()
            return "death"

        output = (NN.NN().brain([self.x, self.y, self.health, self.food, self.is_Starving, self.direction]))[0]
        self.direction = round(output) 
        self.move(self.direction, self.x, self.y, self.velocity)
