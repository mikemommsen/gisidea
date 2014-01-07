
class Node(object):
    """"""
    def __init__(self, parent=None, children=None, oid=None):
        """"""
        self.oid=oid
        self.parent=parent
        self.children=children

    def __str__(self):
        basestring = 'Node object oid: {0}, parent: {1}, children: {2}'
        return basestring.format(self.oid, self.parent, self.children)
        
class Tree(object):
    """"""
    def __init__(self, inlist=None, max_levels=None):
        inlist = sorted(inlist)
        medianIndex = len(inlist) / 2
        median = inlist[medianIndex]
        
        
    def rotate(self):
        
        
        
    
    
  
