from rotatable import Rotatable
import pygame
import math

class Polygon(Rotatable):
    def __init__(self,x,y,dx,dy,rotation,world_width,world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mOriginalPolygon = []
        self.mColor = (255, 255, 255)
        
    def getPolygon(self):
        return self.mOriginalPolygon
    
    def getColor(self):
        return self.mColor
    
    def setPolygon(self,point_list):
        self.mOriginalPolygon = point_list
        
    def getRadius(self):
        total = 0
        if self.mOriginalPolygon == []:
            return 0
        for (x,y) in self.mOriginalPolygon:
            d = math.sqrt(x**2 + y**2)
            total += d
        return total/len(self.mOriginalPolygon)
    
    def setColor(self,color):
        self.mColor = color
    
    def draw(self,surface):
        point_list = self.mOriginalPolygon[::]
        point_list = self.rotateAndTranslatePointList(point_list)
        pygame.draw.polygon(surface, self.mColor, point_list, 1)