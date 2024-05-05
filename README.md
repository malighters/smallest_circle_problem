# Smallest Circle Problem Solver

This program provides a graphical interface to solve the smallest circle problem for a set of random points.

## Requirements
- Python 3
- Tkinter library

## Installation
No installation is necessary. Just ensure you have Python 3 installed on your system.
If you do not have Tkinter library already installed on your system then use this command
``` bash
sudo apt-get install python3-tk
```

## Usage
1. Run the `main.py` script using Python.
2. Enter the number of points you want to generate in the input field labeled "Number of points."
3. Click on the "Add Point" button to randomly generate the specified number of points on the canvas.
4. Once points are added, click on the "Draw circle" button to compute and draw the smallest circle enclosing all the points.
5. To clear the canvas and start over, click on the "Clear Canvas" button.

## Files
- `main.py`: The main script that generates the graphical interface and handles user interactions.
- `circle.py`: Contains functions for computing the smallest enclosing circle for a set of points.

## How it Works
The program generates random points within a specified region on the canvas. It then computes the smallest circle that encloses all these points using an efficient algorithm implemented in `circle.py`. The computed circle is drawn on the canvas.

## Algorithm
The algorithm used to compute the smallest enclosing circle is based on randomized incremental algorithm. It works by adding points one by one and maintaining the smallest enclosing circle as new points are added.