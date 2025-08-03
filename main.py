import creature
import time
import math
import random
import NN
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

Creatures = [creature.Creature(window, max_screen_x, max_screen_y) for i in range(10)]

def update():
    print('update()')
    for i in range(len(Creatures)):
        print(Creatures[i].update())

if __name__ == "__main__":
    main()
