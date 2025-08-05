from graphics import *
import tkinter as tk
import main

width = 700
height = 700

window = GraphWin("Pablo Evolution a-1.2", width, height)
window.setBackground('black')


window.setCoords(0, 0, width, height)


entries = []

mutation_chance = Entry(Point(width/2, height * 0.9), 15)
mutation_chance.setFill("white")
mutation_chance.setText("Mutation chance")
mutation_chance.setTextColor("red")
mutation_chance.setSize(20)
mutation_chance.draw(window)
entries.append(mutation_chance)

mutation_amount = Entry(Point(width/2, height * 0.8), 15)
mutation_amount.setFill("white")
mutation_amount.setText("Mutation amount")
mutation_amount.setTextColor("red")
mutation_amount.setSize(20)
mutation_amount.draw(window)
entries.append(mutation_amount)

food = Entry(Point(width/2, height * 0.7), 15)
food.setFill("white")
food.setText("Food amount")
food.setTextColor("red")
food.setSize(20)
food.draw(window)
entries.append(food)

cell = Entry(Point(width/2, height * 0.6), 15)
cell.setFill("white")
cell.setText("Cell amount")
cell.setTextColor("red")
cell.setSize(20)
cell.draw(window)
entries.append(cell)

fps = Entry(Point(width/2, height * 0.5), 15)
fps.setFill("white")
fps.setText("FPS")
fps.setTextColor("red")
fps.setSize(20)
fps.draw(window)
entries.append(fps)

def on_submit(entries):

    values = [entry.getText() for entry in entries]
    print("User input:", values)
    mutation_chance = float(values[0])
    mutation_amount = float(values[1])
    food = int(values[2])
    cells = int(values[3])
    fps = int(values[4])
    main.main(mutation_chance, mutation_amount, food, cells, fps)
    window.close()
    window.master
    quit()
    

def submit_command():

    on_submit(entries)


button = tk.Button(window.master, text="Submit", command=submit_command)

window.create_window(width/2, height - 50, window=button)

window.master.mainloop()
