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
    
    def centralpoint(self):
        """returns the point that has the lowest total distance"""
        mylist = []
        for p in self.points:
            # dont need to remove point because distance to itself is zero
            mylist.append((p,self.totaldistance(p)))
        return sorted(mylist, key = lambda x: x[1])[0][0]
    
    @classmethod
    def closest(inlist, inpoint):
        """returns the closest point to the inpoint from the collection"""
        return sorted(inlist, key = lambda x: x.distance(inpoint))[0]
        
    def median(self):
        """returns a new point which is the median point for the point collection"""
        # we could think about using an inverse distance function here
        numberpoints = len(self.points)
        middle = numberpoints / 2
        if  numberpoints % 2 == 0:
            medianx = sum(sorted(self.xs)[middle - 1:middle]) / 2
            mediany = sum(sorted(self.ys)[middle - 1:middle]) / 2
        else:
            medianx = sorted(self.xs)[middle]
            mediany = sorted(self.ys)[middle]
        return Point(medianx, mediany)
       
    @classmethod
    def findneighbors(pointlist, inpoint):
        closest = self.closest(inpoint)
        perpindicular = inpoint.perpindicular(closest)
        for i in pointlist:
            if perpindicular.isright(i): 
                pointlist.remove(i)
        return pointlist, closest
    
    def middlestep(self, inpoint):
        pointlist = self.points
        mylist = []
        while pointlist:
            pointlist, closest = findneighbors(pointlist, inpoint)
            mylist.append(closest)
        return mylist
            
            
    def voronoi(self):
        for i in self.points:
            self.middlestep(i)
        
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
  
