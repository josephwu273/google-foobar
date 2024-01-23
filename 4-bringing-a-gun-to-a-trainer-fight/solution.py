from math import sqrt, ceil


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

    def reflectX(self, c=0):
        #Reflects point acros the line x=c
        #This allows subclasses to return an instance of themself rather than of Point
        return self.__class__(2*c-self.x, self.y)
    
    def reflectY(self, c=0):
        #Reflects point acros the line x=c
        return self.__class__(self.x, 2*c-self.y)

    def reflectXY(self):
        return self.__class__(-self.x, -self.y)

    def distanceTo(self, op):
        return sqrt((op.x-self.x)**2 + (op.y-self.y)**2)

    def vectorTo(self, op):
        x = op.x-self.x
        y = op.y-self.y
        g = gcd(x,y)
        return (x/g, y/g)


class Guard(Point):
    pass


class Player(Point):
    pass


def expand_room(room, player, guard, dis):
    xlen, ylen = room
    max_x = float(player.x+dis)
    max_y = float(player.y+dis)
    xrooms = int(ceil(max_x/xlen))
    yrooms = int(ceil(max_y/ylen))
    image_players = [[None]*yrooms for _ in range(xrooms)]
    image_players[0][0] = player
    image_guards = [[None]*yrooms for _ in range(xrooms)]
    image_guards[0][0] = guard
    for i in range(xrooms):
        for j in range(yrooms):
            if j==0:
                if i==0:
                    continue
                else:
                    image_players[i][j] = image_players[i-1][j].reflectX(i*xlen)
                    image_guards[i][j] = image_guards[i-1][j].reflectX(i*xlen)
            else:
                image_players[i][j] = image_players[i][j-1].reflectY(j*ylen)
                image_guards[i][j] = image_guards[i][j-1].reflectY(j*ylen)
    targets = sum(image_players, []) + sum(image_guards, [])
    return targets
            

def expand_quadrants(targets):
    qii = map(lambda p: p.reflectY(), targets)
    qiii = map(lambda p: p.reflectXY(), targets)
    qiv = map(lambda p: p.reflectX(), targets)
    return targets + qii + qiii + qiv


def sort_and_filter(targets, dist, origin):
    f = filter(lambda p : p.distanceTo(origin)<=dist, targets)
    f.sort(key = lambda p:p.distanceTo(origin))
    return f

def get_vectors(targets, origin):
    vectors = dict()
    while targets:
        t = targets.pop(0)
        if t.distanceTo(origin)==0:
            continue
        else:
            v = origin.vectorTo(t)
            if v not in vectors:
                vectors[v] = t
    return vectors


def guard_count(vectors):
    targets = vectors.values()
    guards = sum(isinstance(t, Guard) for t in targets)
    return guards


def solution(dimensions, your_position, trainer_position, distance):
    player = Player(your_position)
    guard = Guard(trainer_position)
    qi_targets = expand_room(dimensions, player, guard, distance)
    all_targets = expand_quadrants(qi_targets)
    sf = sort_and_filter(all_targets, distance, player)
    vectors = get_vectors(sf, player)
    guards = guard_count(vectors)
    return guards
