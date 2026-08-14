import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
TITLE = "Eco Quiz!"
score = 0
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
           Question("What colour is the recycle bin?",["Black","Green","Blue","Brown"],2),
           Question("What food is poisonous to parrots?",["Cookies","Seeds","Leaves","Parrot food"],1),
           Question("What plant can you make paper from?",["Rose","Money Plant","Shrubs","Sugar Cane"],4),
           Question("What is the most popular form of green energy?",["Hydro-electric","Wind","Solar","Biomass"],3),
           Question("Which one of these soils is fertile?",["Brown-Earth","Peat","Podzol","Sand"],1)
        ]
        self.current = 0
        self.score = 0
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        self.buttons = []
        options = self.questions[self.current].options
        self.buttons.append(Button(70,250,200,80,options[0]))
        self.buttons.append(Button(500,250,200,80,options[1]))
        self.buttons.append(Button(70,450,200,80,options[2]))
        self.buttons.append(Button(500,450,200,80,options[3]))

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
        pygame.draw.rect(screen,"CadetBlue",self.rect)
        text = font.render(self.text,True,"white")
        screen.blit(text,(self.rect.x+15,self.rect.y+10))

    def click(self,position):
        return self.rect.collidepoint(position)
button1 = Button(30,250,200,80,"Black")
quiz = Quiz()
while run == True:
    screen.fill("DarkOrchid")
    font = pygame.font.SysFont("Oswald",30)

    quiz.draw(screen,font)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_number = 1
            for button in quiz.buttons:
                if button.click(pygame.mouse.get_pos()):
                    if button_number == quiz.questions[quiz.current].correct_answer:
                        pygame.draw.rect(screen,"lime",button.rect)
                        text = font.render(button.text,True,"white")
                        screen.blit(text,(button.rect.x+15,button.rect.y+10))
                        pygame.display.update()
                        pygame.time.delay(3000)
                        score += 1
                        quiz.current += 1
                        if quiz.current < 5:
                            quiz.create_buttons()
                    else:
                        quiz.current += 1
                        if quiz.current <5:
                            quiz.create_buttons()
                button_number +=1

    if quiz.current == 5:
        font = pygame.font.SysFont("Oswald",70)
        text = font.render(f"Finished! your score is {score}/5!",True,"white")
        screen.fill("black")
        screen.blit(text,(100,300))
        pygame.display.update()
        pygame.time.delay(5000)
        run = False
    pygame.display.update()
