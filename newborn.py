from tkinter import*
from random import randint
import time

gui=Tk()

def znajdywanie(event):
    return(event.x, event.y)

c=Canvas(gui, width=800, height=800, bg='white')
c.bind('<Motion>', znajdywanie)
c.pack()

gui.mainloop()
