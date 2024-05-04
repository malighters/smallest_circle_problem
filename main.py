import tkinter as tk
import random

# Points array
points = []

# Create a tkinter window
window = tk.Tk()
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
# Setting tkinter window size
window.geometry("%dx%d" % (width, height))
window.title("Smallest circle problem")

# Create a canvas widget
canvas = tk.Canvas(window, width=1920, height=1080)

# Function to add a point to the canvas
def add_point():
    for i in range(int(points_entry.get())):
        x = random.randint(320, 1920-320)
        y = random.randint(180, 1080-180)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='black')
        points.append((x, y))

# Function to clear the canvas
def clear_canvas():
    canvas.delete('all')

# Create a label and entry for number 
points_label = tk.Label(window, text="Number of points:")
points_label.pack()
points_entry = tk.Entry(window)
points_entry.pack()

# Create a button to add a point
add_button = tk.Button(window, text="Add Point", command=add_point)
add_button.pack()

# Create a button to clear the canvas
clear_button = tk.Button(window, text="Clear Canvas", command=clear_canvas)
clear_button.pack()

# Pack the canvas widget
canvas.pack()

# Start the tkinter event loop
window.mainloop()