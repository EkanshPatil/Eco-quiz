import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
TITLE = "Eco Quiz!"

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

run = True

class Question():
    def __init__(self,text,options,correct_answer):
        self.question = text
        self.options = options
        self.correct_answer = correct_answer
question1 = Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green")


class Quiz():
    def __init__(self):
        self.questions = [
           Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green"),
           Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green"),
           Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green"),
           Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green"),
           Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],"Green")
        ]
        self.current = 0
        self.score = 0
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        self.buttons = []
        for option in self.questions[self.current].options:
            self.buttons.append(Button(30,250,200,80,option))

    def draw(self,screen,font):
       question = self.questions[self.current]
       text = font.render(question.question,True,"white")
       screen.blit(text,(40,40))
       for button in self.buttons:
           button.draw(screen,font)


class Button():
    def __init__(self,x,y,width,height,text):
        self.rect = pygame.Rect(x,y,width,height)
        self.text = text

    def draw(self,screen,font):
        pygame.draw.rect(screen,"ForestGreen",self.rect)
        text = font.render(self.text,True,"white")
        screen.blit(text,(self.rect.x+15,self.rect.y+10))

    def click(self,position):
        return self.rect.collidepoint(position)
button1 = Button(30,250,200,80,"Black")
quiz = Quiz()
while run == True:
    screen.fill("DarkOrchid")
    font = pygame.font.SysFont("Oswald",30)
    button1.click(pygame.mouse.get_pos())
    quiz.draw(screen,font)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
