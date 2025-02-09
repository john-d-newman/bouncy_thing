
import pygame

class Pipes:
    def __init__(self):
        pass
    x = 750 #this is the left edge of the pipe
    y = 200 # this is the middle of the two pipes
    width = 100 # this is the space between pipes
    top_pipe = pygame.Rect(x, 0, 50, y-(width/2))
    bottom_pipe = pygame.Rect(x, y+(width/2), 50, 400-(y-(width/2)))
    scored = False
    def draw_pipe(self, screen): #this works right now
        self.top_pipe = self.top_pipe.move(self.x, 0) #make new pipe in new posiiont for collision bullshit
        self.top_pipe.update(self.x, 0, 50, self.y-(self.width/2)) #make pipe appear in right place.
        self.bottom_pipe = self.bottom_pipe.move(self.x, 0)
        self.bottom_pipe.update(self.x, self.y+(self.width/2), 50, 400-(self.y-(self.width/2)))
        ##okay so this draws it, but what i want to do, is the difference of them is between the width
        #so x is fine, top  matters, as does y, im not sure height is important
        #top pipe, always x, always 0 top, always 50 width, height is y
        pygame.draw.rect(screen, pygame.colordict.THECOLORS.get("chartreuse"), self.top_pipe)#draw top pipe
        #bottom pipe, always x, ? top, always 50 width, height is 400 - top point, or just make it massive
        pygame.draw.rect(screen, pygame.colordict.THECOLORS.get("chartreuse"), self.bottom_pipe)#draw bottom pipe
    def get_pipes(self):
        return [self.top_pipe,self.bottom_pipe]
