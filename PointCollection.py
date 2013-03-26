import Point

class PointCollection:
    
    def __init__(self, listofpoints):
        self.points = listofpoints
        self.xs = [a.x for a in self.points]
        self.ys = [a.y for a in self.points]
    
    def __str__(self):
        return 'list of points:', [str(x) for x in self.points]
    
    def createbbox(self):
        minimum = Point(min(self.xs),min(self.ys))
        maximum = Point(max(self.xs),max(self.ys))
        self.Bbox = Bbox(minimum, maximum)
    
    def __sum__(self):
        return Point(sum(self.xs), sum(self.ys))
    
    def mean(self):
        return sum(self)/len(self)
        
    def totaldistance(self, inpoint):
        """finds the sum of the distance from inpoint to collection"""
        total = 0
        for point in self.points:
            total += inpoint.distance(point)
        return total
        
    def closest(self, inpoint):
        """returns the closest point to the inpoint from the collection"""
        return sorted(self.points, key = lambda x: x.distance(inpoint))[0]
  
class Bbox:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        
    def __str__(self):
        return 'bbox with mimimum at: {0} and maximum at {1}'.format(str(self.minimum),str(self.maximum))
        
    def inside(self, inpoint):
        if self.minimum.x > inpoint.x > self.maximum.x and self.minimum.y > inpoint.y > self.maximum.y:
            return True
        else:
            return False
  
