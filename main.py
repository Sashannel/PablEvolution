import creature
import time
import math
import random
import NN
import food
from graphics import *
from datetime import datetime

fps = 1000

max_screen_x = 1820
max_screen_y = 980

mutation_chance = 0.9
mutation_amount = 0.5
base_food = 500
base_cells = 100

window = GraphWin("Pablo Evolution", max_screen_x, max_screen_y)
window.setBackground('black')

running = True

Creatures = [creature.Creature(window, max_screen_x, max_screen_y, random.randint(0, max_screen_x),
                               random.randint(0, max_screen_y)) for i in range(base_cells)]
Foods = [food.Food(window, max_screen_x, max_screen_y) for i in range(base_food)]

def main():

    print("main() called")
    frame = 0
    time1 = int(round(time.time() * 1000))
    time2 = int(round(time.time() * 1000))

    textfps = Text(Point(65, 20), "FPS: 0")
    textfps.setTextColor("white")
    textfps.setSize(25)
    textfps.draw(window)

    textcreature = Text(Point(110, 50), "Creatures: 0")
    textcreature.setTextColor("white")
    textcreature.setSize(25)
    textcreature.draw(window)

    textfood = Text(Point(75, 85), "Food: 0")
    textfood.setTextColor("white")
    textfood.setSize(25)
    textfood.draw(window)

    for i in range(1000000):

        update(frame)
        

        time2 = int(round(time.time() * 1000))

        if time2 - time1 * 1000 < 1/fps:

            time.sleep(1/fps)

        if round(1/(time2 - time1 + 1) * 1000) <= fps:

            textfps.setText(f"FPS: {round(1/(time2 - time1 + 1) * 1000)}")

        else:

            textfps.setText(f"FPS: {fps}")
            
        textcreature.setText(f"Creatures: {len(Creatures)}")
        textfood.setText(f"Food: {len(Foods)}")

        frame += 1

        time1 = int(round(time.time() * 1000))


def save_brain_txt(brain, frame, score, network_shape):

    with open(f"best_brain_frame_{frame}.txt", "w") as file:

        file.write("Best brain architecture\n")
        file.write(f"Number of frames survived: {frame}, with {score} food eaten\n")
        file.write(f"Using this shape for the NN: {network_shape}\n")

        for i, layer in enumerate(brain.layers):

            file.write(f"Layer {i}:\n")
            file.write(f"Weights:\n{layer.weights}\n")
            file.write(f"Biases:\n{layer.biases}\n")
            file.write("\n")

    print("Saved the best brain of this simulation")



best_cell = 0
best_brain = Creatures[best_cell].brain
best_frame = 0
best_score = 0

def update(frame):

    global best_cell, best_brain, best_frame, best_score

    if frame % 60 == 0:

        for i in range(random.randint(1, 3)):

            new_food = food.Food(window, max_screen_x, max_screen_y)
            Foods.append(new_food)

    for cell in Creatures[:]:

        if frame >= 300:

            if (cell.time_alive + 1000 * cell.full_score) > (best_frame + 1000 * best_score):

                best_cell = Creatures.index(cell)
                best_brain = cell.brain
                best_frame = cell.time_alive
                best_score = cell.full_score
                

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
                cell.full_score += 1
  
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
                        new_cell.brain = cell.brain.copy()

                        for layer in new_cell.brain.layers:

                            layer.mutate(mutation_chance, mutation_amount, new_cell.brain)


        if cell.update() == "death":

            Creatures.remove(cell)

        if (frame >= 300):

            if len(Creatures) == 0:
                
                save_brain_txt(best_brain, best_frame, best_score, best_brain.networkShape)
                now = datetime.now()
                filename = now.strftime("%Y-%m-%d--%H-%M") + f"--{best_frame}-{best_score}.json"
                best_brain.save(filename)


if __name__ == "__main__":

    main()
