import math

class Point:
    def __init__(self,x=None,y=None,z=None,t=None):
        self.x = x
        self.y = y
        self.z = z
        self.t = t
        
    def __str__(self):
        return 'point at x:{0},y:{1},z:{2},t:{3}'.format(self.x,self.y,self.z,self.t)

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
        
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)
        
    def __mod__(self, other):
        return Point(self.x % other.x, self.y % other.y)
        
    def __pow__(self, other):
        return Point(pow(self.x, other.x), pow(self.y, other.y))

    def __div__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __radd__(self, other):
        return Point(self.x + other, self.y + other)
        
    def __rsub__(self, other):
        return Point(self.x - other, self.y - other)
        
    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)
        
    def __iadd__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __isub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
        
    def __imul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __neg__(self):
        return Point(-(self.x), -(self.y))

    def __pos__(self):
        return Point(+(self.x), +(self.y))
        
    def __abs__(self):
        return Point(abs(self.x), abs(self.y))

    def __invert__(self):
        return Point(~(self.x), ~(self.y))


