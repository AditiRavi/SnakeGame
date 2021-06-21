import random
from turtle import Turtle

COLORS = ["royal blue", "blue", "cyan", "dark orchid", "fuchsia", "purple1", "violet", "aquamarine1", "blue violet"]
print(random.choice(COLORS))


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed(0)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
