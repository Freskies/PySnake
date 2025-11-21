from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = Scoreboard.get_saved_highscore()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    @staticmethod
    def get_saved_highscore():
        with open("highscore.txt", mode="r") as file:
            return int(file.read())

    def save_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))