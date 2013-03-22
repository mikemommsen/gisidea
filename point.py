
class Point:
    def __init__(self,x=None,y=None,z=None,t=None):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __str__(self):
        return 'point at x:{x},y:{y},z:{z},t:{t}'.format(self)


    def distance(self, other):

