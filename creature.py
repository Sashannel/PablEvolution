import NN
from graphics import *
import random
import food

class Creature():

    def __init__(self, window, max_x, max_y, x, y):

        print("New creature created")
        self.x = x
        self.y = y
        self.health = 10
        self.food = 300
        self.score = 0
        self.full_score = 0
        self.is_Starving = False
        self.direction = 4 #0=STOP 1= LEFT 2= RIGHT 3= UP 4= DOWN
        self.velocity = 5
        self.is_Dead = False
        self.window = window
        self.max_x = max_x
        self.max_y = max_y
        self.time_alive = 0
        self.closestX = 10000
        self.closestY = 10000
        rand =  random.randint(1, 4)
        if rand == 1:
            self.brain = NN.NN.create("saved", "model3/2025-08-05--20-20--13509-22.json")
        elif rand == 2:
            self.brain = NN.NN.create("saved", "model3/2025-08-05--21-49--12309-20.json")
        elif rand==3:
            self.brain = NN.NN.create("saved", "model3/2025-08-05--21-55--14709-24.json")
        elif rand==4:
            self.brain = NN.NN.create("saved", "model3/2025-08-05--21-51--12909-21.json")
        self.nn = NN
        self.shape = Circle(Point(self.x, self.y), 7)
        self.shape.setFill('blue')
        self.shape.draw(window)

    def move(self, direction, velocity):

        if direction == 0: #STOP

            self.shape.move(0, 0)
            self.x = self.x
            self.y = self.y

        elif direction == 1: #LEFT

            if self.x - velocity  >= 0:

                self.shape.move(-velocity, 0)
                self.x = self.x - velocity
                self.y = self.y

            else:

                pass

        elif direction == 2: #RIGHT

            if self.x + velocity <= self.max_x:

                self.shape.move(velocity, 0)
                self.x = self.x + velocity
                self.y = self.y

            else:

                pass

        elif direction == 3: #UP

            if self.y - velocity >= 0:

                self.shape.move(0, -velocity)
                self.x = self.x
                self.y = self.y - velocity

            else:

                pass

        elif direction == 4: #DOWN

            if self.y + velocity <= self.max_y:
                self.shape.move(0, velocity)
                self.x = self.x
                self.y = self.y + velocity

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
        
        if self.x > self.max_x:

            self.x = self.max_x

        if self.x < 0:

            self.x = 0

        if self.y > self.max_y:

            self.y = self.max_y

        if self.y < 0:

            self.y = 0

        output = (self.brain.brain([
            self.x, self.y, self.health, self.food, self.is_Starving, self.direction, self.score, self.closestX, self.closestY,
            self.time_alive
            ]))[0]
        self.direction = round(output) 
        self.move(self.direction, self.velocity)
        self.time_alive += 1
