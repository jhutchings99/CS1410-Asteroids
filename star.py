from circle import Circle
import random

class Star(Circle):
    def __init__(self,x,y,world_width,world_height):
        super().__init__(x,y,0,0,0,2,world_width,world_height)
        self.mBrightness = random.randint(0,255)
        
    def getBrightness(self):
        return self.mBrightness
    
    def setBrightness(self,brightness):
        if brightness >= 0 and brightness <= 255:
            self.mBrightness = brightness
            self.setColor((brightness,brightness,brightness))
    
    def evolve(self,dt):
        x = random.randrange(3)
        if x == 0:
            self.setBrightness(self.mBrightness+10)
        elif x == 1:
            self.setBrightness(self.mBrightness-10)