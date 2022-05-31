import pygame

from building import Building

class House(Building):
    def __init__(self, pos):
        self.WORKER_COST = 10
        
        super().__init__(pos)
        self.img = pygame.image.load('assets\\house.png').convert()
