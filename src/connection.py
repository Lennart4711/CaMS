import pygame

class Connection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, win, zoom, win_x, win_y, color=(0,0,0)):
        pygame.draw.line(win, color, 
                            ((self.start[0]-win_x)*zoom, (self.start[1]-win_y)*zoom),
                            ((self.end[0]-win_x)*zoom, (self.end[1]-win_y)*zoom)
                        ,int(3*zoom))