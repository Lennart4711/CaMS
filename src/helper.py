import math

def screen_to_world(pos, zoom,win_pos): 
    x = pos[0]/zoom+win_pos[0]
    y = pos[1]/zoom+win_pos[1]
    return x,y
    
def world_to_screen(pos, zoom,win_pos):
    x = (pos[0]-win_pos[0])*zoom
    y = (pos[1]-win_pos[1])*zoom
    return x,y
