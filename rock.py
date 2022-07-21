from polygon import Polygon
from random import uniform, randint
import math

class Rock(Polygon):
    def __init__(self,x,y,world_width,world_height):
        super().__init__(x,y,0,0,uniform(0.0, 359.9),world_width,world_height)
        self.mSpinRate = uniform(-90, 90)
        self.accelerate(uniform(10, 20))
        radius = uniform(10,20)
        number_of_points = randint(5,10)
        self.setPolygon(self.createRandomPolygon(radius,number_of_points))
        
    def createRandomPolygon(self,radius,number_of_points):
        point_list = []
        theta = (2*math.pi)/number_of_points
        for i in range(number_of_points):
            r = uniform(radius*.7,radius*1.3)
            x = r*math.cos(theta*i)
            y = r*math.sin(theta*i)
            point_list.append((x,y))
        return point_list
    
    def getSpinRate(self,):
        return self.mSpinRate

    def setSpinRate(self,spin_rate):
        self.mSpinRate = spin_rate
    
    def evolve(self,dt):
        self.move(dt)
        self.rotate(dt*self.mSpinRate)