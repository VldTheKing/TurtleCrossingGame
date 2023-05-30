from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.current_level}", align="center", font=("Courier", 16, "normal"))

    def increase_level(self):
        self.current_level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", align="center", font=("Arial", 24, "normal"))
