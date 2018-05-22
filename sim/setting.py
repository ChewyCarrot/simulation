from pygame import *
init()


SIZE =  height, width = (1000,700)
screen = display.set_mode(SIZE)
clock = time.Clock()


background = image.load("res/map.png")
tFont = font.SysFont("res/fonts/HACKED", 25)
subFont = font.SysFont("comicsans", 25)


WHITE   =  (255, 255, 255)
GREEN   =  (  0, 255,   0)
PINK    =  (255, 102, 178)              
RED     =  (255,   0,   0)
YELLOW  =  (255, 255,   0) 
ORANGE  =  (255, 120,   0)
BLACK   =  (  0,   0,   0)
GREY    =  ( 32,  32,  32)