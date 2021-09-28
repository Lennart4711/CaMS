import pygame
import random
import math


class Worker:
    def __init__(self, building, color = (1,1,123)):
        self.color = color
        self.SPEED = 1000
        self.current = building
        self.destination = building
        self.dif_x = 0
        self.dif_y = 0
        self.pos = building.pos.copy()
        
        
        

    def next(self):
        self.current = self.destination
        #self.pos = self.current.pos.copy()
        try:
            self.destination = random.choice(self.current.cons)
        except IndexError:
            print("Add another node")

        self.dif_x = self.destination.pos[0]-self.pos[0]
        self.dif_y = self.destination.pos[1]-self.pos[1]      
            
    def goto(self, building):
        self.destination = building
        self.pos = self.destination.pos.copy()
        self.next()
        

    def walk(self):
        
        if(math.dist(self.pos, self.destination.pos)<10):
           self.next()

        self.pos[0] += self.dif_x/self.SPEED
        self.pos[1] += self.dif_y/self.SPEED
        
        


    def draw(self, win, zoom, win_x, win_y):
        pygame.draw.circle(win, self.color, ((self.pos[0]-win_x)*zoom,(self.pos[1]-win_y)*zoom), 8*zoom)
        
    

