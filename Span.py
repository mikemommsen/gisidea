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
    
    def spanInside(self, other):
        if pointInside(self, other.low) and pointInside(self, other.high):
            return True
        else:
            return False
            
    def touches(self, other):
        if inside(self, other.low) or inside(self, other.high):
            return False
