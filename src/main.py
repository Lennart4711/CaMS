import math
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
from pygame.locals import *


from building import Building
from connection import Connection
from worker import Worker
from mine import Mine
from house import House
import cProfile, pstats, io



def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

class Game():
    def __init__(self):
        self.MIN_ZOOM = 0.35
        self.MAX_ZOOM = 5
        self.FIELD_SIZE = 2000
        self.WIN_X = 1000
        self.WIN_Y = 1000
        self.SPAWN_TIME = 0.5

        self.quit = False
        self.win = pygame.display.set_mode((self.WIN_X, self.WIN_Y))
        pygame.display.set_caption("CaMS")
        self.win_x = 400
        self.win_y = 400
        self.zoom = 3

        self.type = Building
        self.buildings = []
        self.connections = []

        for x in range(20):
            for y in range(20):
                self.add_building(list((x*100,y*100)))
                
                
        self.workers = []
        self.workers.append(Worker(self.buildings[0]))     
        for _ in range(1000):
            self.workers.append(Worker(self.buildings[210]))     

        self.last = time.time()
                



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

        for connection in self.connections:
            connection.draw(self.win, self.zoom, self.win_x, self.win_y)
        
        for building in self.buildings:
            building.draw(self.win, self.zoom, self.win_x, self.win_y, )
        
        for worker in self.workers:
            worker.draw(self.win, self.zoom, self.win_x, self.win_y)
        pygame.display.flip()

    def input(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                print("Stopping the game...")
                self.quit = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                before = self.screen_to_world(pygame.mouse.get_pos())

                if event.button == 4 and self.zoom < self.MAX_ZOOM:
                    self.resize(1.1, before)
                elif event.button == 5 and self.zoom > self.MIN_ZOOM:
                    self.resize(0.9, before)
                elif event.button == 1:
                    #add building and corresponding connections
                    nearest = 1000
                    build = True
                    for building in self.buildings:
                        distance = math.dist(self.screen_to_world(pygame.mouse.get_pos()), building.pos)
                        if(distance < nearest):
                            nearest = distance
                        if(distance < 100):
                            build = False 
                    
                    if(build and nearest < 200):
                        self.add_building(list(self.screen_to_world(pygame.mouse.get_pos())))
                        
                elif event.button == 3:
                    for building in self.buildings:
                        distance = int(math.dist(self.screen_to_world(pygame.mouse.get_pos()), building.pos))
                            
                        if(distance < 40):
                            self.workers[0].goto(building)            
                            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_PLUS] and time.time()-self.last>self.SPAWN_TIME:
            self.last = time.time()
            self.workers.append(Worker(self.buildings[0]))

        self.move(keys)

        if keys[pygame.K_1]:
            self.type = Building
        elif keys[pygame.K_2]:
            self.type = House
        elif keys[pygame.K_3]:
            self.type = Mine
        

    def move(self, keys):
        if keys[pygame.K_LEFT]:
                self.win_x -=2/self.zoom
        elif keys[pygame.K_RIGHT]:
                self.win_x +=2/self.zoom

        if keys[pygame.K_UP]:
                self.win_y -=2/self.zoom
        elif keys[pygame.K_DOWN]:
                self.win_y += 2/self.zoom

    def resize(self, factor, before):
        self.zoom *= factor
        after = self.screen_to_world(pygame.mouse.get_pos())
        
        offset = before[0]-after[0],before[1]-after[1]
        self.win_x += offset[0]
        self.win_y += offset[1]

    def add_building(self, pos):
        self.buildings.append(self.type(pos))
        for building in self.buildings:
            if(building is not self.buildings[-1] and (math.dist(self.buildings[-1].pos, building.pos)<200)):
                self.connections.append(Connection(building.pos,self.buildings[-1].pos))
                building.cons.append(self.buildings[-1])
                self.buildings[-1].cons.append(building)

    def building_logic(self):
        for building in self.buildings:
            building.update()

    def worker_logic(self):
        for worker in self.workers:
            worker.walk()
    @profile
    def update(self):
        self.building_logic()
        self.worker_logic()
        time1 = time.time()

        self.draw()
        time2 = time.time()
        self.input()    
        
    def start(self):
            self.quit = False
            while(not self.quit): 
                self.update()
               


if __name__ == '__main__':
    game = Game()
    game.start()