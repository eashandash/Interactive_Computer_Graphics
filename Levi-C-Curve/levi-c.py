import pygame
import math

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('Levi-c curve')


def c_curve(x,y,l,angle,n):

	if n==1:
		pygame.draw.line(screen,(255,255,255),(x,y),(x+l*math.cos(math.radians(angle)),y+l*math.sin(math.radians(angle))) )
		pygame.display.update()

	else:
		levi_c(x,y,l/math.sqrt(2),angle+45,n-1)
		levi_c(x+l*math.cos(math.radians(angle+45))/math.sqrt(2),y+l*math.sin(math.radians(angle+45))/math.sqrt(2),l/math.sqrt(2),angle-45,n-1)


l,angle,n = (float(x) for x in input('Please enter the value of l, angle, n\n').strip().split(' '))
c_curve(300,200,l,angle,n)



