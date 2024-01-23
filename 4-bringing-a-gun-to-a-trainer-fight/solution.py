from math import sqrt


def gcd(a, b):
	while(b):
	    a, b = b, a%b
	return abs(a)


class Point:
    def __init__(self, *args):
        #single argument passed in as an iterable
        if len(args)==1:
            self.x, self.y = args[0]
        elif len(args)==2:
            self.x, self.y = args
        else:
            raise ValueError("oops")
    
    def __repr__(self):
        c = self.__class__.__name__
        return c + str((self.x, self.y))
 
    def reflectX(self):
        #This allows subclasses to return an instance of themself rather than of Point
        return self.__class__(self.x,-self.y)
    
    def reflectY(self):
        return self.__class__(-self.x, self.y)

    def reflectXY(self):
        return self.__class__(-self.x, self.y)

    def distanceTo(self, op):
        return sqrt((op.x-self.x)**2 + (op.y-self.y)**2)

    def vectorTo(self, op):
        x = op.x-self.x
        y = op.y-self.y
        g = gcd(x,y)
        return [x/h, y/g]


class Guard(Point):
    pass


class Player(Point):
    pass


class Room:
    def __init__(self, xlen, ylen, player, guard):
        self.xlen = xlen
        self.ylen = ylen
        self.player = player
        self.guard = guard
    
    def expand_room(self):
        foo = self.dist/xlen+1 # ceil()
        bar = self.dist/ylen+1
        fake_players = []
        fake_guards = []