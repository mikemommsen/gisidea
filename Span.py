class Span:
    """basic exercise of a 1d span to work through basic concepts"""
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.length = high - low

    def pointInside(self, invalue):
        if self.low < invalue < self.high:
            return True
        else:
            return False
            
    def pointOutside(self, invalue):
        if self.low > invalue or self.high < invalue:
            return True
        else:
            return False

    def pointOnBoundary(self, invalue):
        if self.low == invalue or invalue == self.high:
            return True
        else:
            return False
    
    def disjoint(self, other):
        if self.low > other.high or self.high < other.low:
            return True
        else:
            return False
            
    def overlapping(self, other):
        if self.pointInside(other.low) and self.pointOutside(other.high):
            return True
        elif self.pointOutside(other.low) and self.pointInside(other.high):
            return True
        else:
            return False
            
    def nested(self, other):
        if self.low < other.low and self.high > other.high:
            return True
        else:
            return False
            
    def equal(self, other):
        if self.low == other.low and self.high == other.high:
            return True
        else:
            return False
    
    def touchesOutside(self, other):
        if self.pointOnBoundary(other.low) and self.pointIntside(other.high):
            return True
        elif self.pointOnBoundary(other.high) and self.pointIntside(other.low):
            return True
        else: 
            return False
            
    def touchesInside(self, other):
        if self.pointOnBoundary(other.low) and self.pointOutside(other.high):
            return True
        elif self.pointOnBoundary(other.high) and self.pointOutside(other.low):
            return True
        else: 
            return False
    # these set operations might fit into the iterable span idea, because they need to return multiples
class ListOfSpans:
    def __init__(self, inlist = None):
        self.spans = inlist
    
    @classmethod
    def spansFromList(inlist, lowerbound=None, upperbound=None):
        """takes a list of values and creates spans which are the closest to each point"""
        inlist = sorted(inlist)
        mylist = [lowerbound]
        spanlist = []
        for i in range(len(inlist) - 1):
            mylist += [sum(inlist[i:i+1])/2]
        mylist += [upperbound]
        for i in range(len(mylist) - 1):
            spanlist.append(Span(mylist[i],mylist[i+1]))
        return spanlist
    
    def union(self, other):
        
    def intersect(self, other):
    
    def symmetric_difference(self, other):
        
    def difference(self, other):
