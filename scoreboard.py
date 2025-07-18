from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.num}", align="center", font=('Arial', 12, 'normal'))
    
    def add_score(self):
        self.num += 1
        self.clear()
        self.write(f"Score: {self.num}", align="center", font=('Arial', 12, 'normal'))