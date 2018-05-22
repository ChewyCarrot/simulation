from pygame import *
from setting import *
init()

pPos = [Rect(100,250,50,50)]

mainRect = [Rect(300,50,150,25),
            Rect(500,50,150,25),
            Rect(50,100,200,25)]

MtxtRect = [Rect(310, 55, 150, 25),
            Rect(510, 55, 150, 25)]

maintxt = [tFont.render("Start Simulation", True, BLACK),
           tFont.render("Stop Simulation", True, BLACK)]


subRect = [Rect(50,100,200,25),
           Rect(50,125,200,25),
           Rect(50,150,200,25),
           Rect(50,175,200,25),
           Rect(50,200,200,25)]

StxtRect = [Rect(60,105,100,25),
            Rect(60,130,200,25),
            Rect(60,155,200,25),
            Rect(60,180,200,25),
            Rect(60,205,200,25)]


subtxt = [subFont.render("--None--", True, BLACK),
          subFont.render("H.I.V", True, BLACK),
          subFont.render("MALARIA", True, BLACK),
          subFont.render("TUBERCULOSIS", True, BLACK),
          subFont.render("BUBONIC PLAGUE", True, BLACK)]