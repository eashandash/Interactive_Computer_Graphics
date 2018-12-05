from graphics import *
import time
import random


class dance:
    def __init__( self, x, y, index=0 ):
        self.current = index
        self.image = None
        self.x  = x
        self.y  = y
        
    def move( self, dx, dy ):
        x, y = self.x, self.y
        if self.image != None:
            x = self.image.getAnchor().getX()
            y = self.image.getAnchor().getY()
            self.image.undraw()

        
        if dx > 0:
            self.current = ( self.current + 1 ) % 20
        else:
            self.current = ( self.current + 10 - 1 ) % 20            

        self.image = Image( Point( x, y ),
                            "walk%d.gif" % self.current )
        self.image.draw( self.win )

    def draw( self, win ):
        self.win = win
        if self.image == None:
            self.image = Image( Point( self.x, self.y ),
                            "walk%d.gif" % self.current )
            self.image.draw( win )
                            
                            

def stickman():
    W = 800
    H = 600
    win = GraphWin( "stickman", W, H )
    
    walker = dance( W/2, H/ 2 )
    walker.draw( win )
    
    while True:
        walker.move( 5, 0 )
        time.sleep( 0.12 )

    win.getMouse()
    win.close()



def main():
    stickman()
    
                        
main()