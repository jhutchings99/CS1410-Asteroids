import math

class Movable:
    def __init__(self, x, y, dx, dy, world_width, world_height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mActive = True
        
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    def getActive(self):
        return self.mActive
    
    def setActive(self, value):
        self.mActive = value
    
    def hits(self, other):
        d = math.sqrt((other.mX-self.mX)**2+(other.mY-self.mY)**2)
        if d <= self.getRadius() + other.getRadius():
            return True
        else:
            return False
    
    def move(self, dt):
        self.mX += self.mDX * dt
        self.mY += self.mDY * dt
        
        if self.mX >= self.mWorldWidth:
            self.mX -= self.mWorldWidth
        elif self.mX < 0:
            self.mX += self.mWorldWidth
            
        if self.mY >= self.mWorldHeight:
            self.mY -= self.mWorldHeight
        elif self.mY < 0:
            self.mY += self.mWorldHeight
        
    def accelerate(self, delta_velocity):
        raise NotImplementedError('You must implement accelerate in a child class')
    
    def evolve(self, dt):
        raise NotImplementedError('You must implement evolve in a child class')
    
    def draw(self, surface):
        raise NotImplementedError('You must implement draw in a child class')
    
    def getRadius(self):
        raise NotImplementedError('You must implement getRadius in a child class') 