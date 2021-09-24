import pygame

class Building():
    def __init__(self, pos,width):
        self.pos = pos
        self.x, self.y = pos
        
        self.width = width
        self.img = pygame.image.load('assets\house.png')
      
        

    def draw(self, win, zoom, win_x, win_y, color=(0,0,0)):
        
        win.blit(   #img
                    pygame.transform.scale(self.img, (int(32*zoom),int(32*zoom))),
                    (#pos
                        (self.x-win_x)*zoom-16*zoom, 
                        (self.y-win_y)*zoom-16*zoom
                    )
                )
        

    