from ship import Ship
from rock import Rock
from bullet import Bullet
from star import Star
from random import randrange

class Asteroids:
    def __init__(self,world_width,world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = Ship(world_width/2,world_height/2,world_width,world_height)
        self.mRocks = []
        for i in range(10):
            rock = Rock(0,0,world_width,world_height)
            self.mRocks.append(rock)
        self.mBullets = []
        self.mStars = []
        for i in range(20):
            star = Star(randrange(0, world_width), randrange(0, world_height), world_width, world_height)
            self.mStars.append(star)
        self.mObjects = [self.mShip] + self.mRocks + self.mStars + self.mBullets
        
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    def getShip(self):
        return self.mShip
    
    def getRocks(self):
        return self.mRocks
    
    def getStars(self):
        return self.mStars
    
    def getBullets(self):
        return self.mBullets
    
    def getObjects(self):
        return self.mObjects
    
    def turnShipLeft(self,delta_rotation):
        self.mShip.rotate(-delta_rotation)
    
    def turnShipRight(self,delta_rotation):
        self.mShip.rotate(delta_rotation)
    
    def accelerateShip(self,delta_velocity):
        self.mShip.accelerate(delta_velocity)
        
    def fire(self):
        if len(self.mBullets) <= 2:
            b = self.mShip.fire()
            self.mBullets.append(b)
            self.mObjects.append(b)
    
    def evolveAllObjects(self,dt):
        for obj in self.mObjects:
            obj.evolve(dt)
    
    def collideShipAndBullets(self):
        if self.mShip.getActive():
            for b in self.mBullets:
                if b.hits(self.mShip):
                    self.mShip.setActive(False)
                    b.setActive(False)
    
    def collideShipAndRocks(self):
        if self.mShip.getActive():
            for r in self.mRocks:
                if r.hits(self.mShip):
                    self.mShip.setActive(False)
                    r.setActive(False)
    
    def collideRocksAndBullets(self):
        for r in self.mRocks:
            if r.getActive():
                for b in self.mBullets:
                    if b.getActive():
                        if b.hits(r):
                            r.setActive(False)
                            b.setActive(False)
    
    def removeInactiveObjects(self):
        temp_bullets = []
        for obj in self.mBullets:
            if obj.getActive():
                temp_bullets.append(obj)
        self.mBullets = temp_bullets
        
        temp_rocks = []
        for obj in self.mRocks:
            if obj.getActive():
                temp_rocks.append(obj)
        self.mRocks = temp_rocks
        
        if self.mShip.getActive():
            self.mObjects = [self.mShip] + self.mRocks + self.mStars + self.mBullets 
        
    def evolve(self,dt):
        self.evolveAllObjects(dt)
        self.collideShipAndBullets()
        self.collideShipAndRocks()
        self.collideRocksAndBullets()
        self.removeInactiveObjects()
    
    def draw(self,surface):
        surface.fill((0,0,0))
        for obj in self.mObjects:
            if obj.getActive():
                obj.draw(surface)
