from turtle import Turtle
FONT = ("Courier", 12, "normal")
ALIGNMENT="centre"
ALIGNMENT2="centre"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-40, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT)



    def game_over(self):
        self.goto(0, -270)
        self.write("GAME OVER", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
