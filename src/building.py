import pygame

class Building():
    def __init__(self, pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        

        self.img = pygame.image.load('assets\house.png')
        self.cons = []
        

    def draw(self, win, zoom, win_x, win_y):
        
        win.blit(   #img
                    pygame.transform.scale(self.img, (int(32*zoom),int(32*zoom))),
                    (#pos
                        (self.x-win_x)*zoom-16*zoom, 
                        (self.y-win_y)*zoom-16*zoom
                    )
                )
        
 
    