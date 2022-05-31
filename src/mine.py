from building import Building
from mineral import Mineral
import pygame

class Mine(Building):
    def __init__(self, pos):
        self.MINING_SPEED = 5000
        
        super().__init__(pos)
        self.img = pygame.image.load('assets\\mine.png').convert()
        self.counter = 0

    def update(self):
        self.counter += 1
        if(self.counter == self.MINING_SPEED):
            self.minerals.append(Mineral(1))
            self.counter = 0

    
        

