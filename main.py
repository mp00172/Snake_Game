from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from messages import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
STARTING_SPEED_DELAY_IN_SECS = 0.12
ACCELERATION_STEP = 0.005
FOOD_DISTANCE_BUFFER = 17

game_speed = STARTING_SPEED_DELAY_IN_SECS

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")

screen.title("Snake Game")
screen.tracer(0)


def reset_screen():
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)


welcome_message()

scoreboard = Scoreboard(screenwidth=SCREEN_WIDTH, screenheight=SCREEN_HEIGHT)

program_running = True

while program_running:

    snake = Snake()
    food = Food(screenwidth=SCREEN_WIDTH, screenheight=SCREEN_HEIGHT)
    scoreboard.print_score()

    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    screen.update()

    game_running = True

    while game_running:
        snake.move()
        time.sleep(game_speed)
        screen.update()
        if snake.wall_collision(screenwidth=SCREEN_WIDTH, screenheight=SCREEN_HEIGHT) or snake.tail_collision():
            game_running = False
            scoreboard.apply_highscore()
            if not play_again(player_score=scoreboard.score, highscore=scoreboard.highscore):
                program_running = False
            else:
                reset_screen()
                game_speed = STARTING_SPEED_DELAY_IN_SECS
                scoreboard.reset()
        if snake.head.distance(food) < FOOD_DISTANCE_BUFFER:
            scoreboard.score_up()
            scoreboard.print_score()
            snake.add_square()
            if scoreboard.score % 2 == 0:
                game_speed -= ACCELERATION_STEP
            food.reappear()

screen.bye()
