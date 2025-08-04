import creature
import time
import math
import random
import NN
import food
from graphics import *

fps = 60

max_screen_x = 1820
max_screen_y = 980

mutation_chance = 0.1
mutation_amount = 2
base_food = 500
base_cells = 1000

window = GraphWin("Pablo Evolution", max_screen_x, max_screen_y)
window.setBackground('black')

running = True

def main():

    frame = 0
    time1 = int(round(time.time() * 1000))
    time2 = int(round(time.time() * 1000))

    text = Text(Point(65, 20), "FPS: 0")
    text.setTextColor("white")
    text.setSize(25)
    text.draw(window)

    for i in range(100000):

        update(frame)
        

        time2 = int(round(time.time() * 1000))

        if time2 - time1 * 1000 < 1/fps:

            time.sleep(1/fps)

        if round(1/(time2 - time1 + 1) * 1000) <= fps:
            text.setText(f"FPS: {round(1/(time2 - time1 + 1) * 1000)}")
        else:
            text.setText(f"FPS: {fps}")

        frame += 1

        time1 = int(round(time.time() * 1000))

Creatures = [creature.Creature(window, max_screen_x, max_screen_y, random.randint(0, max_screen_x),
                               random.randint(0, max_screen_y)) for i in range(base_cells)]
Foods = [food.Food(window, max_screen_x, max_screen_y) for i in range(base_food)]

def update(frame):

    if frame % 60 == 0:

        new_food = food.Food(window, max_screen_x, max_screen_y)
        Foods.append(new_food)

    for cell in Creatures[:]:

        closestDistance = 10000
        closestID = 0

        for food_item in Foods[:]:

            if math.sqrt((cell.x - food_item.x) ** 2 + (cell.y - food_item.y) ** 2) < closestDistance:

                closestDistance = math.sqrt((cell.x - food_item.x) ** 2 + (cell.y - food_item.y) ** 2)
                closestID = Foods.index(food_item)
                cell.closestX = food_item.x
                cell.closestY = food_item.y

            if math.sqrt((cell.x - food_item.x) ** 2 + (cell.y - food_item.y) ** 2) < 7:

                cell.food += 600
                cell.score += 1
                Foods.remove(food_item)
                food_item.is_Dead = True
                food_item.update()

                if cell.score == 2:

                    cell.score = 0

                    for i in range(random.randint(1, 3)):

                        new_x = random.randint(cell.x - 20, cell.x + 20)
                        new_y = random.randint(cell.y - 20, cell.y + 20)
                        new_cell = creature.Creature(window, max_screen_x, max_screen_y, new_x, new_y)
                        Creatures.append(new_cell)
                        new_cell.brain.layers = cell.nn.copyLayers()

                        for layer in new_cell.brain.layers:

                            layer.mutate(mutation_chance, mutation_amount, new_cell.brain)


        if cell.update() == "death":

            Creatures.remove(cell)


if __name__ == "__main__":

    main()
