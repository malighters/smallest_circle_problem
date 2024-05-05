import tkinter as tk
import random
from circle import make_circle

points = []

window = tk.Tk()
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Smallest circle problem")

canvas = tk.Canvas(window, width=width, height=height)

def add_point():
    for i in range(int(points_entry.get())):
        x = random.randint(width*0.25, width*0.75)
        y = random.randint(height*0.25, height*0.75)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
        points.append((x, y))

def clear_canvas():
    points.clear()
    canvas.delete('all')

def draw_circle():
    if (len(points) != 0):
        circle_x, circle_y, circle_radius = make_circle(points)
        canvas.create_oval(circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius, outline='blue', width=5)

points_label = tk.Label(window, text="Number of points:")
points_label.pack(anchor='w')

points_entry = tk.Entry(window)
points_entry.pack(anchor='w')

add_button = tk.Button(window, text="Add Point", command=add_point)
add_button.pack(anchor='w')

clear_button = tk.Button(window, text="Clear Canvas", command=clear_canvas)
clear_button.pack(anchor='w')

circle_button = tk.Button(window, text="Draw circle", command=draw_circle)
circle_button.pack(anchor='w')

canvas.pack()

window.mainloop()