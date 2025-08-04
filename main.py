import creature
import time
import math
import random
import NN
import food
from graphics import *

fps = 60

max_screen_x = 1536
max_screen_y = 864

window = GraphWin("Pablo Evolution", max_screen_x, max_screen_y)
window.setBackground('black')

running = True

def main():

    for i in range(100000):

        print("Main.py executed")
        update()
        time.sleep(1/fps)
        print("Updated the program!")

Creatures = [creature.Creature(window, max_screen_x, max_screen_y, random.randint(0, max_screen_x), random.randint(0, max_screen_y)) for i in range(10)]
Foods = [food.Food(window, max_screen_x, max_screen_y) for i in range(300)]

def update():

    print('update()')

    for cell in Creatures[:]:
        closestDistance = 10000
        closestID = 0
        for food in Foods[:]:
            
            if math.sqrt((cell.x - food.x) ** 2 + (cell.y - food.y) ** 2) < closestDistance:

                closestDistance = math.sqrt((cell.x - food.x) ** 2 + (cell.y - food.y) ** 2)
                closestID = Foods.index(food)
                cell.closestX = food.x
                cell.closestY = food.y

            if math.sqrt((cell.x - food.x) ** 2 + (cell.y - food.y) ** 2) < 7: #checking if the cell can eat this food

                cell.food += 600
                cell.score += 1
                Foods.remove(food)
                food.is_Dead = True
                food.update()

                if cell.score == 2:

                    cell.score = 0
                    new_x = random.randint(cell.x - 10, cell.x + 10)
                    new_y = random.randint(cell.y - 10, cell.y + 10)
                    Creatures.append(creature.Creature(window, max_screen_x, max_screen_y, new_x, new_y))

        if cell.update() == "death":

            Creatures.remove(cell)
            print(cell, "is dead")

if __name__ == "__main__":
    main()
