from polygon import Polygon
from bullet import Bullet

class Ship(Polygon):
    def __init__(self,x,y,world_width,world_height):
        super().__init__(x, y, 0, 0, 0, world_width, world_height)
        self.setPolygon([(10,0),(-10,10),(0,0),(-10,-10)])
        
    def fire(self):
        (x,y) = self.mOriginalPolygon[0]
        (x,y) = self.rotateAndTranslatePoint(x,y)
        b = Bullet(x,y,self.mDX,self.mDY,self.mRotation,self.mWorldWidth,self.mWorldHeight)
        return b
    
    def evolve(self,dt):
        self.move(dt)