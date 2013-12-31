class Span:
    """basic exercise of a 1d span to work through basic concepts"""
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.length = high - low

    def pointInside(self, invalue):
        """"""
        if self.low < invalue < self.high:
            return True
        else:
            return False
            
    def pointOutside(self, invalue):
        """"""
        if self.low > invalue or self.high < invalue:
            return True
        else:
            return False

    def pointOnBoundary(self, invalue):
        """"""
        if self.low == invalue or invalue == self.high:
            return True
        else:
            return False
    
    def disjoint(self, other):
        """"""
        if self.low > other.high or self.high < other.low:
            return True
        else:
            return False
            
    def overlapping(self, other):
        """"""
        if self.pointInside(other.low) and self.pointOutside(other.high):
            return True
        elif self.pointOutside(other.low) and self.pointInside(other.high):
            return True
        else:
            return False
            
    def nested(self, other):
        """"""
        if self.low < other.low and self.high > other.high:
            return True
        else:
            return False
            
    def equal(self, other):
        """"""
        if self.low == other.low and self.high == other.high:
            return True
        else:
            return False
    
    def touchesOutside(self, other):
        """"""
        if self.pointOnBoundary(other.low) and self.pointIntside(other.high):
            return True
        elif self.pointOnBoundary(other.high) and self.pointIntside(other.low):
            return True
        else: 
            return False
            
    def touchesInside(self, other):
        """"""
        if self.pointOnBoundary(other.low) and self.pointOutside(other.high):
            return True
        elif self.pointOnBoundary(other.high) and self.pointOutside(other.low):
            return True
        else: 
            return False
    
    def union(self, other):
        """"""
        if not self.disjoint(other):
            low = min(self.low, other.low)
            high = max(self.high, other.high)
            return Span(low, high)
        else:
            return None
        
    def intersect(self, other):
        """find the area where they are the same"""
        if not self.disjoint(other):
            low = max(self.low, other.low)
            high = min(self.high, other.high)
            return Span(low, high)
        else:
            return None
    
    
    def symmetric_difference(self, other):
        """return both differences - might be faster to chain the logic than call difference twice"""
        return self.difference(other), other.difference(self)
        
    def difference(self, other):
        """"""
        return
