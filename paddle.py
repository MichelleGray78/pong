from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.penup()
        self.goto(starting_position)
        self.resizemode("user")
        self.shapesize(5, 1)

    # Move paddles
    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        