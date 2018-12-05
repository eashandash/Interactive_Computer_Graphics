# EASHAN DASH
# CED15I043
# PROBLEM : NON INTERSECTING DISJOINT CIRCLES 

# EACH CIRCLE : RADIUS 10
#               THICKNESS 1





import pygame
from pygame.locals import QUIT

WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
TEXTCOLOR = (  0,   0,  0)
(width, height) = (400, 400)






pygame.init()
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption('circle')
screen.fill(WHITE)


def drawCircle():
    #ctr=10
    for i in range (2,1000,15):

        pygame.draw.circle(screen, GREEN, (i,i), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+70,i), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+40,i), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+160,i+15), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+260,i+15), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+360,i+15), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+460,i+15), 10, 1)
        pygame.draw.circle(screen, GREEN, (i+560,i+15), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+610,i+15), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+110,i+5), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+210,i+10), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+310,i+15), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+410,i+20), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+510,i+25), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+710,i+15), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+660,i+15), 10, 1)
        # pygame.draw.circle(screen, GREEN, (i+760,i+15), 10, 1)

        
        #pygame.draw.circle(screen, BLUE, (230,230), ctr+40+i, 5)
        #pygame.draw.circle(screen, RED, (230,230), ctr+50+i , 5)
        #pygame.draw.circle(screen, GREEN, (230,230), ctr+15+i, 3)
        #ctr=ctr+30

        
    pygame.display.flip()
    while True:
            for evt in pygame.event.get():
                if evt.type == QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.display.update()


drawCircle()



