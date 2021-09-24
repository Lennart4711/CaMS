import math
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
pygame.init()

from building import Building
from connection import Connection


class Game():
    def __init__(self):
        self.MIN_ZOOM = 0.5
        self.MAX_ZOOM = 2
        self.FIELD_SIZE = 2000
        self.WIN_X = 1000
        self.WIN_Y = 1000
        

        self.quit = False
        self.win = pygame.display.set_mode((self.WIN_X, self.WIN_Y))
        self.win_x = 0
        self.win_y = 0
        self.zoom = 1

        self.clock = pygame.time.Clock()


        self.buildings = []
        self.connections = []


    def screen_to_world(self, pos):
        x = pos[0]/self.zoom+self.win_x
        y = pos[1]/self.zoom+self.win_y
        return x,y
    
    def world_to_screen(self, pos):
        x = (pos[0]-self.win_x)*self.zoom
        y = (pos[1]-self.win_y)*self.zoom
        return x,y

    

    def draw(self):
        self.win.fill((125,124, 110))
        for building in self.buildings:
            building.draw(self.win, self.zoom, self.win_x, self.win_y)
       
        for connection in self.connections:
            connection.draw(self.win, self.zoom, self.win_x, self.win_y)
      
        pygame.display.flip()

        
    def input(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                print("Stopping the game...")
                self.quit = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                before = self.screen_to_world(pygame.mouse.get_pos())

                if event.button == 4 and self.zoom < self.MAX_ZOOM:
                    self.zoom *= 1.1
                    after = self.screen_to_world(pygame.mouse.get_pos())

                    offset = before[0]-after[0],before[1]-after[1]
                    self.win_x += offset[0]
                    self.win_y += offset[1]
                elif event.button == 5 and self.zoom > self.MIN_ZOOM:
                    self.zoom *= 0.9
                    after = self.screen_to_world(pygame.mouse.get_pos())
        
                    offset = before[0]-after[0],before[1]-after[1]
                    self.win_x += offset[0]
                    self.win_y += offset[1]
                elif event.button == 1:
                    #add building and corresponding connections
                    for building in self.buildings:
                        distance = math.dist(self.screen_to_world(pygame.mouse.get_pos()), building.pos)
                        if(distance < 100):
                            break
                    else:
                        self.buildings.append(Building(self.screen_to_world(pygame.mouse.get_pos()),16))
                        for building in self.buildings:
                            if(building is not self.buildings[-1] and (math.dist(self.buildings[-1].pos, building.pos)<200)):
                                self.connections.append(Connection(building.pos,self.buildings[-1].pos))
      
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
                self.win_x -=2/self.zoom
        elif keys[pygame.K_RIGHT]:
                self.win_x +=2/self.zoom

        if keys[pygame.K_UP]:
                self.win_y -=2/self.zoom
        elif keys[pygame.K_DOWN]:
                self.win_y += 2/self.zoom

    
    def update(self):
        self.draw()
        self.input()    
    
    def start(self):
            self.quit = False
            while(not self.quit): 
                self.update()

if __name__ == '__main__':
    game = Game()
    game.start()