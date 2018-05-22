from pygame import *
from setting import *
from tabs import *


def stxt():
    for i in range (1,5):
        draw.rect(screen, GREY, subRect[i], 3)
    for i in range (1,5):
        screen.blit(subtxt[i], StxtRect[i])

    
def text():  
    for i in range (3):
        draw.rect(screen, GREY, mainRect[i], 3)
    
    for i in range (2):
        screen.blit(maintxt[i], MtxtRect[i])
        
    screen.blit(subtxt[0], StxtRect[0])