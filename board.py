from tkinter import*
from random import randint
import time
import math

gui=Tk()

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class VelocityController:
    
    def __init__(self, vx, vy):
        self.vx = vx
        self.vy = vy
        self.v = math.sqrt(self.vx * self.vx + self.vy * self.vy)
        self.xh = 0
        self.yh = 0

    def start(self):
        frame.bind('<Motion>', self.handle_mouse_event)

    def handle_mouse_event(self, event):
        self.evaluate(event.x, event.y)

    def evaluate(self, xm, ym):
        self.vx = self.recalculate_vx(xm, ym)
        self.vy = self.recalculate_vy(xm, ym)        

    def set_head_pos(self, head_pos):
        self.xh = head_pos.x
        self.yh = head_pos.y
        
    def recalculate_vx(self, xm, ym):
        return((xm - self.xh)/  3)

    def recalculate_vy(self, xm, ym):
        return((ym - self.yh) / 3)        

class SnakeController:

    def __init__(self, velocityController, delay):
        self.delay = delay
        self.velocityController = velocityController

    def start(self):
        self.create_head()
        
        self.velocityController.start()
        self.next_frame()

    def next_frame(self):
        gui.after(self.delay, self.update_frame)

    def get_head_pos(self):
        coords = frame.coords(self.snake_head)
        return(Position(coords[0], coords[1]))

    def update_frame(self):        
        frame.move(self.snake_head, self.velocityController.vx, self.velocityController.vy)    
        self.velocityController.set_head_pos(self.get_head_pos())
        
        self.next_frame()

    def create_head(self):
        self.snake_head = frame.create_rectangle(10, 10, 30, 30, fill = 'white')        

frame = Canvas(gui, width = 800, height = 800, bg = 'black')
frame.pack()

SnakeController(VelocityController(20, 30), 150).start()

gui.mainloop()
