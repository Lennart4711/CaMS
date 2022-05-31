import pygame
import time

class Building():
    def __init__(self, pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        

        self.img = pygame.image.load('assets\\building.png').convert()
        self.gloom = pygame.image.load('assets\\gloom.png')

        self.cons = []
        self.minerals = []

    def draw(self, win, zoom, win_x, win_y):
        # sprite = pygame.transform.scale(self.gloom, (int(128*zoom),int(128*zoom)))

        # win.blit(   #img
        #             sprite,
        #             (#pos
        #                 (self.x-win_x)*zoom-32*zoom, 
        #                 (self.y-win_y)*zoom-32*zoom
        #             )
        #         )

        sprite = pygame.transform.scale(self.img, (int(32*zoom),int(32*zoom)))
        win.blit(   #img
                    sprite,
                    (#pos
                        (self.x-win_x)*zoom-16*zoom, 
                        (self.y-win_y)*zoom-16*zoom
                    )
                )
        


    
    def update(self):
        pass


        
 
    