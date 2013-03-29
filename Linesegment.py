import math, Point

class Linesegment:
    
    def __init__(self, origin, end):
        self.origin = origin
        self.end = end
        self.diff = origin - end
        self.length = origin.distance(end)
        
    def calcAngle(self):
        self.slope = self.diff.y / self.diff.x
        self.atan2 = self.orgin.atan2(self.end)
        self.atan = math.atan2(self.slope)
        
  
    def isleft(self, inpoint):
        
        
    def isright(self, inpoint):
    
