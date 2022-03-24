from tkinter import messagebox


def welcome_message():
    messagebox.showinfo(title="Snake Game", message="Welcome to Snake Game!\n"
                                                    "\n"
                                                    "Press ENTER to start!")


def play_again(player_score, highscore):
    return messagebox.askyesno(title="$%&#%'&## !!!!!!!", message=f"Oops! Game over!\n"
                                                           "\n"
                                                           f"\nYour score: {player_score}"
                                                           f"\nHighscore: {highscore}"
                                                           "\n"
                                                           "\nPlay again?")
