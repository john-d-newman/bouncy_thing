"""
Plyaer class for bouncy game
"""
import pygame

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