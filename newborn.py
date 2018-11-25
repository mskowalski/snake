
from tkinter import*

import random
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

    def __init__(self, velocityController):
        self.velocityController = velocityController

    def start(self):
        self.create_head()        
        self.velocityController.start()

    def get_head_pos(self):
        coords = frame.coords(self.snake_head)
        return(Position(coords[0], coords[1]))

    def get_bodypart_pos(self):
        coords2 = frame.coords(self.snake_bodypart)
        return(Position2(coords2[0], coords2[1]))

    def update_frame(self):        
        frame.move(self.snake_head, self.velocityController.vx, self.velocityController.vy)
        self.velocityController.set_head_pos(self.get_head_pos())        

    def create_head(self):
        self.snake_head = frame.create_rectangle(10, 10, 30, 30, fill = 'white')

    def create_snake_bodypart(self):
        coords = frame.coords(self.snake_head)
        self.snake_bodypart = frame.create_rectangle(coords[3] + 20, coords[1] + 20, coords[3] + 40, coords[1] + 40, fill = 'white')

class AppleController:

    def __init__(self):
        self.x = random.randint(0, 780)
        self.x2 = self.x + 20
        self.y = random.randint(0, 780)
        self.y2 = self.y + 20

    def draw_apple(self):
        self.apple = frame.create_rectangle(self.x, self.y, self.x2, self.y2, fill = 'green')

    def snake_eat_apple(self, snakeController):
        frame.delete(self.apple);        
        self.apple = frame.create_rectangle(self.x, self.y, self.x2, self.y2, fill = 'red')

    def start(self):
        self.draw_apple()        

    def update_frame(self, snakeController):
        self.snake_eat_apple(snakeController)

class BoardController:
    def __init__(self, snakeController, appleController, delay):
        self.snakeController = snakeController
        self.appleController = appleController
        self.delay = delay

    def start(self):
        self.snakeController.start()
        self.appleController.start();
        
        self.next_frame()

    def next_frame(self):
        gui.after(self.delay, self.update_frame)


    def update_frame(self):
        self.snakeController.update_frame()
        self.appleController.update_frame(self.snakeController)

        self.snake_position_check(self.appleController, self.snakeController)
        
        self.next_frame()        

    def snake_position_check(self, appleController, snakeController):
        snake_head_pos = snakeController.get_head_pos()
        if appleController.x <= snake_head_pos.x <= appleController.x2 and appleController.y <= snake_head_pos.y <= appleController.y2:
            self.appleController.snake_eat_apple(self.snakeController)
            self.appleController.draw_apple()
            self.snakeController.create_snake_bodypart()

frame = Canvas(gui, width = 800, height = 800, bg = 'black')
frame.pack()

BoardController(SnakeController(VelocityController(20, 30)), AppleController(), 150).start() 

gui.mainloop()
