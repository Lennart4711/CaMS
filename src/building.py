import pygame

class Building():
    def __init__(self, pos,width):
        self.pos = pos
        self.x, self.y = pos
        
        self.width = width
        self.img = pygame.image.load('assets\house.png')
        self.skip=[]
        

    def draw(self, win, zoom, win_x, win_y, color=(0,0,0)):
        
        win.blit(pygame.transform.scale(self.img, (int(32*zoom),int(32*zoom))), ((self.x-win_x)*zoom-16*zoom, (self.y-win_y)*zoom-16*zoom))
        #äpygame.draw.circle(win, color, ((self.x-win_x)*zoom, (self.y-win_y)*zoom), self.width*zoom)

    