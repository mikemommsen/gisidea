# mikemommsen.com
from operator import attrgetter



class Span(object):
    """basic exercise of a 1d span to work through basic concepts"""
    def __init__(self, low, high):
        if high < low:
            low, high = high, low
        self.low = low
        self.high = high
        self.length = high - low
        self.data = self.low, self.high
    
    def __str__(self):
        return 'Span object: low: {0}, high: {1}, length: {2}'.format(self.low, self.high, self.length)

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
            
    def split(self, invalue):
        """if invalue is inside the span then returns span split at that point.
        if it is outside then we clearly just return the span itself"""
        if self.pointinside(invalue):
            return Spanlist([Span(self.low, invalue), Span(invalue, self.high)])
        else:
            return self
    
    def disjoint(self, other):
        """test to see if two spans are disjoint or not"""
        if self.low > other.high or self.high < other.low:
            return True
        else:
            return False
            
    def overlapping(self, other):
        """returns true if one of the other endpoints is inside the span, but not both"""
        if bool(self.pointInside(other.low)) + bool(self.pointInside(other.high)) == 1:
            return True
        else:
            return False
            
    def nested(self, other):
        """returns True if other.low and other.high are inside the span"""
        if self.low < other.low and self.high > other.high:
            return True
        else:
            return False
            
    def equal(self, other):
        """returns true if the low and high points are the same"""
        if self.low == other.low and self.high == other.high:
            return True
        else:
            return False
    
    def touchesOutside(self, other):
        """returns true if """
        if self.pointOnBoundary(other.low) and self.pointOutside(other.high):
            return True
        elif self.pointOnBoundary(other.high) and self.pointOutside(other.low):
            return True
        else: 
            return False
            
    def touchesInside(self, other):
        """"""
        if self.pointOnBoundary(other.low) and self.pointInside(other.high):
            return True
        elif self.pointOnBoundary(other.high) and self.pointInside(other.low):
            return True
        else: 
            return False
    
    def bounder(self, other):
        """"""
        low = min(self.low, other.low)
        high = max(self.high, other.high)
        return Span(low, high)
        
    def union(self, other):
        """"""
        if self.disjoint(other):
            return self, other
        else:
            return bounder(self, other)
        
    def intersect(self, other):
        """find the area where they are the same"""
        if not self.disjoint(other):
            low = max(self.low, other.low)
            high = min(self.high, other.high)
            return Span(low, high)
        else:
            return None
        
    def difference(self, other):
        """"""
        if self.disjoint(other):
            return self
        else:
            if self.low < other.low:
                firstspan = Span(self.low, other.low)
            else:
                firstspan = None
            if self.high > other.high:
                secondspan = Span(other.high, self.high)
            else:
                secondspan = None
            return [x for x in (firstspan, secondspan) if x]
            
    def symmetric_difference(self, other):
        """return both differences - might be faster to chain the logic than call difference twice"""
        return self.difference(other), other.difference(self)
        
    def create_frequency(self, other):
        """"""
        if self.disjoint(other):
            return {self: 1, other: 1}
        else:
            intersect = self.intersect(other)
            lowspan = Span(self.low, other.low)
            highspan = Span(self.high, other.high)
            return {lowspan: 1, highspan: 1, intersect: 2}
            
class SpanList(object):
    """"""
    def __init__(self, spans=None):
        """"""
        self.spans = spans
        if spans:
            low = min(getattr(s, 'low') for s in spans)
            high = max(getattr(s, 'high') for s in spans)
        else:
            low = None
            high = None
        self.boundingspan = Span(low, high)

    def __str__(self):
        """"""
        return 'SpanList object with spans: [{0}]'.format(','.join(str(s) for s in self.spans))
        
    def append(self, inSpan):
        self.spans.append(inSpan)
        if inSpan.low < self.low:
            self.low = inSpan.low
        if inSpan.high > self.high:
            self.high = inSpan.high
            
    def __add__(self, other):
    def __iadd__(self, other):
        
    def __sub__(self, other):
        
    def __isub__(self, other):
        
    def remove(self, value):
        
    def 
        
    
    
    def loop_group(self):
        """function to loop through the groups that overlap each other.
        this is nice for some other functions"""
        spans = sorted(self.spans, key=attrgetter('low'))
        prev = spans[0]
        outlist = SpanList([prev])
        for s in spans[1:]:
            if outlist.disjoint(s):
                yield outlist
                outlist = SpanList([s])
            else:
                outlist.append(s)
            prev = s
        else:
            yield outlist
    
    def planarize(self):
        """"""
        self.planar_list = SpanList()
        for s in self.loop_group():
            self.planar_list.append(Span(s.low, s.high))
    
    def frequency_planarize(self):
        """"""
        from collections import Counter
        self.frequency_planar_list = []
        for sGroup in self.loop_group():
            outlist = []
            for s in sGroup:
                low = s.low
                high = s.high
                outlist.append((('low',low), ('high', high)))
            outlist = Counter(outlist)
            looplist = Counter()
            for k, v in outlist.iteritems():
                if k[0] == 'high':
                    v = -v
                looplist[k[1]] += v
            looplist = sorted(looplist.iteritems(), key=lambda x: x[0])
            prevval, count = looplist[0]
            for val, c in looplist[1:]:
                count += c
                self.frequency_planar_list.append(Span(prevval, val,))
                prevval = val
    
    def find_gaps(self):
        """"""
        self.gaps = []
        spans = self.loop_group()
        prevhigh = spans.next()
        for s in spans:
            low, high = s.low, s.high
            outspan = Span(prevhigh, low)
            self.gaps.append(outspan)
            prevhigh = high
            
        
class Tree(object):
    """"""
    def __init__(self, root=None, levels=None
        
        
        
        
        
