from turtle import Turtle
SNAKE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake = []
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for self.position in self.starting_position:
            self.add_snake(self.position)

    def add_snake(self, position):
        self.new_snake = Turtle("square")
        self.new_snake.color("white")
        self.new_snake.penup()
        self.new_snake.goto(position)
        self.snake.append(self.new_snake)


    def extend(self):
        self.add_snake(self.snake[-1].position())

    def move(self):
        for self.num in range(len(self.snake) - 1, 0, -1):
            self.x = self.snake[self.num - 1].xcor()
            self.y = self.snake[self.num - 1].ycor()
            self.snake[self.num].goto(self.x, self.y)
        
        self.snake[0].forward(SNAKE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)