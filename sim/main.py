from pygame import *
from tabs import *
from setting import *
from text import *
init()



subCat = False


running = True
while running: 
    screen.fill(WHITE)
    for evnt in event.get():            
        if evnt.type == QUIT:
            running = False
            
        if evnt.type == MOUSEBUTTONDOWN:
            if mainRect[2].collidepoint(mouse.get_pos()):
                if evnt.button == 1:
                    subCat = True
            else:
                subCat = False
    if subCat == True:
        stxt()


    screen.blit(background,pPos[0])
    text()  
    display.update()