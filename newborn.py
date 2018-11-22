from tkinter import*
from random import randint
import time
import math

gui=Tk()

def handle_mouse_event(event):
    move_head(event)
    return(event.x, event.y)

c=Canvas(gui, width=800, height=800, bg='white')
c.bind('<Motion>', handle_mouse_event)

bodypart= c.create_rectangle(10,10,20,20, fill='black')

def move_head(event):
    c.move(bodypart, event.x, event.y)

c.pack()

gui.mainloop()
