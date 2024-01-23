"""
This solution relies on the trick from physics that to simulate perfect collisions
in a room, you can simply reflect the room over its own walls
"""


from math import sqrt, ceil


def gcd(a, b):
    #Python 2 doesn't have gcd() so we write our own with Euler's algorithm
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
        #Reflects point acros the line y=c
        return self.__class__(self.x, 2*c-self.y)

    def reflectXY(self):
        return self.__class__(-self.x, -self.y)

    def distanceTo(self, op):
        #Distance from this point to other point op
        return sqrt((op.x-self.x)**2 + (op.y-self.y)**2)

    def vectorTo(self, op):
        #Gets the vector (in simplest terms) from this point to other point op
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
    #The max distance we can shoot affects...
    max_x = float(player.x+dis)
    max_y = float(player.y+dis)
    #... the number of image rooms we need to consider
    xrooms = int(ceil(max_x/xlen))
    yrooms = int(ceil(max_y/ylen))
    #Each cell represents an image room. It contains the image player and his coordinates
    image_players = [[None]*yrooms for _ in range(xrooms)]
    image_players[0][0] = player
    image_guards = [[None]*yrooms for _ in range(xrooms)]
    image_guards[0][0] = guard
    #Envision a rectangle with bottom-left corner on the origin
    #This loop builds columns of image-rooms by flipping rooms across its top wall
    #Once a column is complete, make a new column by flipping the bottom room across its right wall
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
    #Flatten out and combine the guards and players into a single list of targets
    targets = sum(image_players, []) + sum(image_guards, [])
    return targets
            

def expand_quadrants(targets):
    # Reflect points from Quadrant I (Cartesian plane) into II, III, and IV
    qii = map(lambda p: p.reflectY(), targets)
    qiii = map(lambda p: p.reflectXY(), targets)
    qiv = map(lambda p: p.reflectX(), targets)
    return targets + qii + qiii + qiv


def sort_and_filter(targets, dist, origin):
    # Remove all targets outside our distance range
    f = filter(lambda p : p.distanceTo(origin)<=dist, targets)
    # Sort remaining targets by distance
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
                #aiming in direction v will hit t 
                vectors[v] = t
            else:
                #Aiming in direction v will hit vectors[v] first so ignore t
                pass
    return vectors


def guard_count(vectors):
    #Count all guards that we will hit
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
