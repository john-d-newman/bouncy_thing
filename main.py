"""
Author: John newman
Created: 2/5/25
modified: 2/5/25
desc: main file, run this and it will play the game, probably just fucking crash at the end though

"""

import pygame
import time
import random

background_color = (0,0,0)
green = pygame.colordict.THECOLORS.get("chartreuse")
red = pygame.colordict.THECOLORS.get("crimson")
mistyrose = pygame.colordict.THECOLORS.get("mistyrose")
navy = pygame.colordict.THECOLORS.get("navy")

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("This is my window, there are many like it but this one is mine")
screen.fill(background_color)
pygame.display.flip()

pygame.font.init()

my_font = pygame.font.SysFont('Candara', 60)

score_rect = pygame.Rect(350, 10, 100, 40)


class Player:
    def __init__(self):
        pass
    x = 120
    y = 200.0
    vert_speed = 0
    player_rect = pygame.Rect(x,y, 40, 20)

    def set_y(self, y):
        self.y = y
        self.player_rect.y = y

class Pipes:
    def __init__(self):
        pass
    x = 750 #this is the left edge of the pipe
    y = 200 # this is the middle of the two pipes
    width = 100 # this is the space between pipes
    top_pipe = pygame.Rect(x, 0, 50, y-(width/2))
    bottom_pipe = pygame.Rect(x, y+(width/2), 50, 400-(y-(width/2)))
    scored = False
    def draw_pipe(self): #this works right now
        self.top_pipe = self.top_pipe.move(self.x, 0) #make new pipe in new posiiont for collision bullshit
        self.top_pipe.update(self.x, 0, 50, self.y-(self.width/2)) #make pipe appear in right place.
        self.bottom_pipe = self.bottom_pipe.move(self.x, 0)
        self.bottom_pipe.update(self.x, self.y+(self.width/2), 50, 400-(self.y-(self.width/2)))
        ##okay so this draws it, but what i want to do, is the difference of them is between the width
        #so x is fine, top  matters, as does y, im not sure height is important
        #top pipe, always x, always 0 top, always 50 width, height is y
        pygame.draw.rect(screen, green, self.top_pipe)#draw top pipe
        #bottom pipe, always x, ? top, always 50 width, height is 400 - top point, or just make it massive
        pygame.draw.rect(screen, green, self.bottom_pipe)#draw bottom pipe
    def get_pipes(self):
        return [self.top_pipe,self.bottom_pipe]

##TODO
"""
Score
varible speed
spice?
Main menu

"""

def main():
    start = time.time() #this is when the game starts, used to make pipes
    last = time.time()
    new = time.time()
    player = Player()
    temp_pipe = Pipes()
    pipes = [temp_pipe]
    #pipes.append(temp_pipe)
    score = 0
    top_text = "Score :"
    running = True
    print('Hello world')
    while running:
        delta = new - last
        last = time.time()
        screen.fill(background_color)
        events =  pygame.event.get()
        for event in events: #input logic, ignore for now
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.vert_speed -= 200
                if event.key == pygame.K_UP:
                    temp_pipe.y += 10
                if event.key == pygame.K_DOWN:
                    temp_pipe.y -= 10
                if event.key == pygame.K_LEFT:
                    temp_pipe.width += 10
                if event.key == pygame.K_RIGHT:
                    temp_pipe.width -= 10
            if event.type == pygame.QUIT:
                running = False
        
        if last-start > 5:
            start = time.time() #reset time
            new_pipe = Pipes()
            new_pipe.y = random.randrange(50,350)
            pipes.append(new_pipe)
        
        ## now this is game logic
        ##display the guy at the x,y spot
        player.set_y(player.y + (player.vert_speed*delta))
        if player.y > 380:
            player.set_y(380)
            player.vert_speed = 0
        if player.y < 0:
            player.set_y(0)
            player.vert_speed = 0

        for pipe in pipes:
            pipe.draw_pipe()
        pygame.draw.rect(screen, (255,255,0), player.player_rect)
        pygame.draw.rect(screen, mistyrose, score_rect)
        text_surface = my_font.render(str(score), False, navy)
        screen.blit(text_surface, (390,0))
        
        pygame.display.flip() ##updating screen

        for pipe in pipes:
            pipe_list = pipe.get_pipes()
            for pip in pipe_list:##TODO efficienyy in this check#okay, player should only check pipe with similar x to iself? i mean that efficient, but could just not
                # pygame.draw.rect(screen, red, pip)
                # pygame.display.flip()
                if player.player_rect.colliderect(pip):
                    print("YOU HIT THE FUCKING WALL")
                    screen.fill(red)
                    my_font2 = pygame.font.SysFont('Comic Sans MS', 240)
                    text_surface = my_font2.render(str(score), False, navy)
                    screen.blit(text_surface, (390,100))
                    pygame.display.flip()
                    dummy = True
                    while dummy:
                        events = pygame.event.get()
                        for event in events:
                            if event.type == pygame.KEYDOWN:
                                pygame.quit()
                                quit(0)



    
        ##gravity logic? every frame take decrease player vert speed by grav
        for pipe in pipes:
            pipe.x -= 100*delta
            if pipe.x < 70 and not pipe.scored:
                pipe.scored = True
                score += 1
                
            if pipe.x < 0:
                pipes.remove(pipe)
        #temp_pipe.x -= 50*delta
        player.vert_speed += 400*delta
        new = time.time()
        
        print(score)


if __name__ == "__main__":
    main()