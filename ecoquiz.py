import pygame

WIDTH = 800
HEIGHT = 600
TITLE = "Eco Quiz!"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

run = True

class Question():
    def __init__(self,text,options,correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
question1 = Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green")

class Player():
    def __init__(self,score):
        self.score = score

while run == True:
    screen.fill("DarkOrchid")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()