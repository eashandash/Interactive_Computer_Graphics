
import pygame
import sys
from pygame import gfxdraw

from pygame.locals import QUIT

class MyBasicGraphics:

    # colors definition
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (227, 27, 27)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    RCB = (27, 27, 27)

    def __init__(self,title):
        pygame.init()  #initialize all imported pygame modules

        self.DISPSURF = pygame.display.set_mode((320, 250), 0, 32)
        pygame.display.set_caption(title)

        # Fill the background with a color
        self.DISPSURF.fill(self.RCB)

        





  