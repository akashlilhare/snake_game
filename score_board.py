from turtle import Turtle, color
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__() 
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.write(f"Score : {self.score}",  align=ALIGNMENT, font=FONT)



    def increase_score(self) :
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}",  align="center", font=("Arial", 22, "normal"))

    def game_over(self) :
        self.goto(0,0)
        self.write("Game Over", align= ALIGNMENT, font=FONT)
        

        

