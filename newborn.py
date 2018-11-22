from tkinter import*
from random import randint
import time
import math

class MouseCoords:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_head(self, event):
        c.move(bodypart, event.x - self.x, event.y - self.y)
        self.x = event.x
        self.y = event.y

def handle_mouse_event(event):
    print(currentMouseCoords.x, " ", currentMouseCoords.y)
    currentMouseCoords.move_head(event)
    return(event.x, event.y)

gui=Tk()
c=Canvas(gui, width=800, height=800, bg='white')

currentMouseCoords = MouseCoords(10, 10)
bodypart= c.create_rectangle(currentMouseCoords.x,currentMouseCoords.y,20,20, fill='black')
c.bind('<Motion>', handle_mouse_event)

c.pack()
gui.mainloop()
