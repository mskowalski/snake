from tkinter import*
from random import randint
import time
import math

class MouseCoords:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_head(self, x, y):
        frame.move(bodypart, vx, vy)
        self.x = x
        self.y = y

def handle_mouse_event(event):    
    currentMouseCoords.move_head(event.x, event.y)    
    return(event.x, event.y)

def move():
    frame.move(bodypart, vx, vy)
    gui.after(delay, move) 
    

gui = Tk()
frame = Canvas(gui, width = 800, height = 800, bg = 'white')

currentMouseCoords = MouseCoords(10, 10)
dv = 20
vx = 20
vy = 30
delay = 250
bodypart = frame.create_rectangle(currentMouseCoords.x, currentMouseCoords.y, 20, 20, fill = 'black')

frame.bind('<Motion>', handle_mouse_event)    
frame.pack()

gui.after(delay, move)
gui.mainloop()

