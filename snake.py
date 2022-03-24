from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.next_segment_position = (0, 0)
        for i in range(3):
            square = Turtle(shape="square")
            square.penup()
            square.goto(self.next_segment_position)
            square.color("white")
            self.snake_segments.append(square)
            self.head = self.snake_segments[0]
            self.next_segment_position = (
            self.snake_segments[-1].position()[0] - 20, self.snake_segments[-1].position()[1])

    def move(self):
        for seg_pos in range(len(self.snake_segments) - 1, 0, -1):
            self.next_segment_position = self.snake_segments[seg_pos - 1].position()
            self.snake_segments[seg_pos].goto(self.next_segment_position)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_square(self):
        square = Turtle(shape="square")
        square.penup()
        square.goto(self.next_segment_position)
        square.color("white")
        self.snake_segments.append(square)
        self.next_segment_position = (self.snake_segments[-1].position()[0] - 20, self.snake_segments[-1].position()[1])

    def wall_collision(self, screenwidth, screenheight):
        if self.head.xcor() <= (-(screenwidth // 2) + 10) or \
                self.head.xcor() >= screenwidth // 2 - 20 or \
                self.head.ycor() <= (-(screenheight // 2) + 20) or \
                self.head.ycor() >= screenheight // 2 - 5:
            return True
        else:
            return False

    def tail_collision(self):
        for segment in self.snake_segments[-1:2:-1]:
            if self.head.distance(segment) < 20:
                return True
        return False
