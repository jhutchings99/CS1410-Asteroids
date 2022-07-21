from movable import Movable
import math

class Rotatable(Movable):
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation
        
    def getRotation(self):
        return self.mRotation
    
    def rotate(self,delta_rotation):
        self.mRotation += delta_rotation
        
        if self.mRotation < 0:
            self.mRotation += 360
        elif self.mRotation >= 360:
            self.mRotation -= 360
    
    def splitDeltaVIntoXAndY(self,rotation,delta_velocity):
        theta = math.radians(rotation)
        x = delta_velocity*math.cos(theta)
        y = delta_velocity*math.sin(theta)
        return (x,y)
    
    def accelerate(self,delta_velocity):
        (dx, dy) = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        self.mDX += dx
        self.mDY += dy
    
    def rotatePoint(self,x,y):
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y,x)
        theta += math.radians(self.mRotation)
        x = r*math.cos(theta)
        y = r*math.sin(theta)
        return (x,y)
        
    def translatePoint(self,x,y):
        x += self.mX
        y += self.mY
        return (x,y)
        
    def rotateAndTranslatePoint(self,x,y):
        (x,y) = self.rotatePoint(x,y)
        (x,y) = self.translatePoint(x,y)
        return (x,y)
    
    def rotateAndTranslatePointList(self,point_list):
        new_list = []
        for (x,y) in point_list:
            (x,y) = self.rotateAndTranslatePoint(x,y)
            new_list.append((x,y))
        return new_list