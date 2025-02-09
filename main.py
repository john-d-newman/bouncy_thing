"""
Author: John newman
Created: 2/5/25
modified: 2/5/25
desc: main file, run this and it will play the game, probably just fucking crash at the end though

"""

import pygame
import time
import random

from player import Player
from pipe import Pipes


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
            pipe.draw_pipe(screen)
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