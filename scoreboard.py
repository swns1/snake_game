from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.num = 0
        self.highscore = 0
        self.penup()
        self.goto(-0, 280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.num}    High Score: {self.highscore}", align="center", font=('Arial', 12, 'normal'))
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.num}    High Score: {self.highscore}", align="center", font=('Arial', 12, 'normal'))

    def add_score(self):
        self.num += 1
        self.update_scoreboard()

    def reset(self):
        if self.num > self.highscore:
            self.highscore = self.num
        self.num = 0
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over.", align="center", font=('Arial', 12, 'normal'))