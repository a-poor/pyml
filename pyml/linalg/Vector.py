
from pprint import pformat

class Vector:
    def __init__(self,data,vertical=True):
        self._data = list(data)
        assert self._data
        self.vertical = vertical

    def __str__(self):
        return pformat(self._data)

    def __repr__(self):
        direction = "V" if self.vertical else "H"
        return f"<Vector.{direction} {self._data}>"

    def __len__(self):
        return len(self._data)

    def __getitem__(self,index):
        return self._data[index]

    def __setitem__(self,index,newdata):
        self._data[index] = newdata

    def __iter__(self):
        return iter(self._data)

    @property
    def T(self):
        return Vector(self._data, not self.vertical)

    
    def __eq__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a==b for a,b in zip(self,other)],self.vertical)
        else:
            return Vector([a == other for a in self],self.vertical)
    
    def __req__(self,other):
        return self == other

    def __ne__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a != b for a,b in zip(self,other)],self.vertical)
        else:
            return Vector([a != other for a in self],self.vertical)

    def __rne__(self,other):
        return self != other

    def __lt__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a < b for a,b in zip(self,other)],self.vertical)
        else:
            return Vector([a < other for a in self],self.vertical)

    def __rlt__(self,other):
        return self >= other

    def __le__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a <= b for a,b in zip(self,other)],self.vertical)
        else:
            return Vector([a <= other for a in self],self.vertical)

    def __rle__(self,other):
        return self > other

    def __gt__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a > b for a,b in zip(self,other)],self.vertical)
        else:
            return Vector([a > other for a in self],self.vertical)

    def __rgt__(self,other):
        return self <= other

    def __ge__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a >= b for a,b in zip(self,other)],self.vertical)
        else:
            return Vector([a >= other for a in self],self.vertical)

    def __rge__(self,other):
        return self < other

    def __or__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a or b for a, b in zip(self,other)],self.vertical)
        else: raise Exception("Can only OR with another Vector")

    def __and__(self,other):
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([a and b for a, b in zip(self,other)],self.vertical)
        else: raise Exception("Can only AND with another Vector")

    def __xor__(self,other):
        xor = lambda a, b: (a and not b) or (not a and b)
        if isinstance(other,Vector):
            assert len(self) == len(other) and self.vertical == other.vertical
            return Vector([xor(a,b) for a, b in zip(self,other)],self.vertical)
        else: raise Exception("Can only XOR with another Vector")

    def __invert__(self):
        return Vector([not n for n in self],self.vertical)

    def any(self):
        return any(self._data)

    def all(self):
        return all(self._data)

    def __add__(self,other):
        assert isinstance(other,(Vector,int,float))
        if isinstance(other,Vector):
            assert len(other) == len(self) and other.vertical == self.vertical
            return Vector([ a+b for a,b in zip(self,other) ],self.vertical)
        else:
            return Vector([a+other for a in self],self.vertical)

    def __radd__(self,other):
        return self + other

    def __sub__(self,other):
        assert isinstance(other,(Vector,int,float))
        if isinstance(other,Vector):
            assert len(other) == len(self) and other.vertical == self.vertical
            return Vector([ a-b for a,b in zip(self,other) ],self.vertical)
        else:
            return Vector([a-other for a in self],self.vertical)

    def __rsub__(self,other):
        assert isinstance(other,(Vector,int,float))
        if isinstance(other,Vector):
            assert len(other) == len(self) and other.vertical == self.vertical
            return Vector([ b-a for a,b in zip(self,other) ],self.vertical)
        else:
            return Vector([other-a for a in self],self.vertical)

    def __mult__(self,other):
        assert isinstance(other,(Vector,int,float))
        if isinstance(other,Vector):
            assert len(other) == len(self) and other.vertical == self.vertical
            return sum([a*b for a,b in zip(self,other)])
        else:
            return Vector([a*other for a in self],self.vertical)

    def __rmult__(self,other):
        return self * other

    def __pow__(self,other):
        return Vector([a**other for a in self],self.vertical)

    def __truediv__(self,other):
        assert isinstance(other,(float,int))
        return self * (1/other)

    # def __rtruediv__(self,other):
    #     pass

    def map(self,fn=lambda n: n):
        return Vector([fn(n) for n in self._data],self.vertical)

    def reduce(self,fn=lambda l, r: l + r,initial=None,*args,**kwargs):
        assert fn.__code__.co_argcount >= 2
        itr = iter(self._data)
        if initial is None:
            l = next(itr)
        else:
            l = initial
        for r in itr:
            l = fn(l,r,*args,**kwargs)
        return l

    def sum(self):
        return sum(self._data)

    def min(self):
        return min(self._data)

    def max(self):
        return max(self._data)

    def mean(self):
        return self.sum() / len(self)

    def median(self):
        n = len(self)
        i, r = divmod(n,2)
        odd = r == 1
        s = sorted(self._data)
        if odd: return s[i]
        else: return (s[i] + s[i+1]) / 2

    def mode(self):
        def make_count(d,n):
            d[n] = d.get(n,0) + 1
            return d
        counts = self.reduce(make_count,{})
        max_n = max(counts.values())
        return [k for k,v in counts.items() if v == max_n]

    def sort(self):
        self._data.sort()

    def sorted(self):
        return Vector(sorted(self._data),self.vertical)


