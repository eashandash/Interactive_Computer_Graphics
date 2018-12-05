
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
        pygame.init()

        self.DISPSURF = pygame.display.set_mode((500, 500))
        pygame.display.set_caption(title)

        # Fill the background with a color
        self.DISPSURF.fill(self.RCB)





    def bresenhams_circle(self,radius,center = (0,0)):
        print("Center is ",center)
        x = 0
        y =  radius

        d = 3-2*radius
        points = []
        # points.append((center[0] + x, center[1] + y))
        # points.append((center[0] + y, center[1] + x))
        # points.append((center[0] + y, center[1] - x))
        # points.append((center[0] + x, center[1] - y))
        # points.append((center[0] - x, center[1] + y))
        # points.append((center[0] - y, center[1] + x))
        # points.append((center[0] - x, center[1] - y))
        # points.append((center[0] - y, center[1] - x))

        while(y >  x):
            x += 1
            if d <= 0:
                d += 4*x + 6
            else:
                
                d += 4*(x-y) + 10
                y -= 1

            points.append((center[0] + x, center[1] + y))
            points.append((center[0] + y, center[1] + x))

            points.append((center[0] + y, center[1] - x))
            points.append((center[0] + x, center[1] - y))

            points.append((center[0] - x, center[1] + y))
            points.append((center[0] - y, center[1] + x))

            points.append((center[0] - x, center[1] - y))
            points.append((center[0] - y, center[1] - x))

        return points
        


    def draw_circle(self,radius,center=(0,0),color =RED):
        points = self.bresenhams_circle(radius,center)

        for pt in points:
            print('ploting point : ',pt)
            gfxdraw.pixel(self.DISPSURF, pt[0] , pt[1],color)
            pygame.display.flip()  #Update the full display Surface to the screen



    def draw_circle1(self,radius,center=(0,0),color =GREEN):
        points = self.bresenhams_circle(radius,center)

        for pt in points:
            print('ploting point : ',pt)
            gfxdraw.pixel(self.DISPSURF, pt[0] , pt[1],color)
            pygame.display.flip()
            


    def draw_circle2(self,radius,center=(0,0),color =BLUE):
        points = self.bresenhams_circle(radius,center)

        for pt in points:
            print('ploting point : ',pt)
            gfxdraw.pixel(self.DISPSURF, pt[0] , pt[1],color)
            pygame.display.flip()                


        #while True:
            #for evt in pygame.event.get():
            #    if evt.type == QUIT:
             #       pygame.quit()
              #      sys.exit()

        pygame.display.update()




graphics  = MyBasicGraphics("BresenhamsCircle Algo")


ctr=10
for i in range(50):
    graphics.draw_circle(center = (250,250),radius = ctr+30+i)
    graphics.draw_circle1(center = (250,250),radius = ctr+40+i)
    graphics.draw_circle2(center = (250,250),radius = ctr+50+i)
    ctr=ctr+10






#graphics.draw_circle1(center = (250,250),radius = 60)






#graphics.draw_circle1(center = (250,250),radius = 35)
#graphics.draw_circle2(center = (250,250),radius = 40)
#graphics.draw_circle(center = (250,250),radius = 45)
#graphics.draw_circle1(center = (250,250),radius = 50)
#graphics.draw_circle2(center = (250,250),radius = 55)
#graphics.draw_circle(center = (250,250),radius = 60)
#graphics.draw_circle1(center = (250,250),radius = 61)




#graphics.draw_circle(center = (250,250),radius = 65)
#graphics.draw_circle1(center = (250,250),radius = 70)
#graphics.draw_circle2(center = (250,250),radius = 75)
#graphics.draw_circle(center = (250,250),radius = 80)
#graphics.draw_circle1(center = (250,250),radius = 85)
#graphics.draw_circle2(center = (250,250),radius = 90)
#graphics.draw_circle(center = (250,250),radius = 95)
#graphics.draw_circle1(center = (250,250),radius = 100)


#graphics.draw_circle(center = (250,250),radius = 120)
#graphics.draw_circle1(center = (250,250),radius = 140)
#graphics.draw_circle2(center = (250,250),radius = 160)
#graphics.draw_circle(center = (250,250),radius = 180)
#graphics.draw_circle1(center = (250,250),radius = 200)
#graphics.draw_circle2(center = (250,250),radius = 220)
#graphics.draw_circle(center = (250,250),radius = 240)
#graphics.draw_circle1(center = (250,250),radius = 260)

#graphics.draw_circle(center = (250,250),radius = 280)
#graphics.draw_circle1(center = (250,250),radius = 300)
#graphics.draw_circle2(center = (250,250),radius = 320)
#graphics.draw_circle(center = (250,250),radius = 340)
#graphics.draw_circle1(center = (250,250),radius = 360)
#graphics.draw_circle2(center = (250,250),radius = 380)
#graphics.draw_circle(center = (250,250),radius = 400)
#graphics.draw_circle1(center = (250,250),radius = 420)