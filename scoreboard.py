from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, screenwidth, screenheight):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto((-(screenwidth // 2) + 20), (screenheight // 2) - 30)

    def print_score(self):
        self.write(f"Score: {self.score}", font=("Arial", 14, "normal"))

    def score_up(self):
        self.score += 1
        self.clear()

    def reset(self):
        self.score = 0

    def apply_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score