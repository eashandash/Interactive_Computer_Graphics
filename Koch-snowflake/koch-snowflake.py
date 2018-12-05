import pygame
import math
import numpy as np

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode([800, 600])
pygame.display.set_caption('KOch curve')


x,y = [300,200]
w = [255,255,255]
b = [0,0,0]


def koch(X,l,angle,n):

	if(n==1):
		z = [l*math.cos(math.radians(angle))/3,l*math.sin(math.radians(angle))/3]
		t = [l*math.cos(math.radians(angle+60))/3,l*math.sin(math.radians(angle+60))/3]

		pygame.draw.line(SCREEN,w,X,[X[0]+z[0],X[1]+z[1]],1)
		pygame.draw.line(SCREEN,b,[X[0]+z[0],X[1]+z[1]],[X[0]+2*z[0],X[1]+2*z[1]],1)
		pygame.draw.line(SCREEN,w,[X[0]+2*z[0],X[1]+2*z[1]],[X[0]+3*z[0],X[1]+3*z[1]],1)
		
		pygame.draw.line(SCREEN,w,[X[0]+z[0],X[1]+z[1]],[X[0]+z[0]+t[0],X[1]+z[1]+t[1]],1)
		pygame.draw.line(SCREEN,w,[X[0]+2*z[0],X[1]+2*z[1]],[X[0]+z[0]+t[0],X[1]+z[1]+t[1]],1)

		pygame.display.update()
	
	else:
		z = [l*math.cos(math.radians(angle))/3,l*math.sin(math.radians(angle))/3]
		t = [l*math.cos(math.radians(angle+60))/3,l*math.sin(math.radians(angle+60))/3]

		koch_snowflake(X,l,angle,n-1)
		
		l=l/3
		koch(X,l,angle,n-1)
		koch([X[0]+z[0],X[1]+z[1]],l,angle+60,n-1)
		koch([X[0]+z[0]+t[0],X[1]+z[1]+t[1]],l,angle-60,n-1)
		koch([X[0]+2*z[0],X[1]+2*z[1]],l,angle,n-1)


l = eval(input("Enter the no of egde length:\n"))
n = eval(input("Enter the no of iterations:\n"))


koch([x,y],l,60,n) #first edge of the traingle
koch([x+l*math.cos(math.radians(60)),y+l*math.sin(math.radians(60))],l,-60,n) #second edge of the triangle
koch([x+l,y],l,180,n)  #third edge of the triangle

