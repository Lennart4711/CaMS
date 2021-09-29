import pygame

from building import Building

class House(Building):
    def __init__(self, pos):
        self.WORKER_COST = 10
        
        super().__init__(pos)
        self.img = pygame.image.load('assets\\house.png')

    def draw(self, win, zoom, win_x, win_y):
        
        win.blit(   #img
                    pygame.transform.scale(self.img, (int(32*zoom),int(32*zoom))),
                    (#pos
                        (self.x-win_x)*zoom-16*zoom, 
                        (self.y-win_y)*zoom-16*zoom
                    )
                )