from math import sqrt

KNIGHT = sqrt(5)

def get_point(n):
    file = n%8
    rank = n//8
    return rank,file

def dist(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def solution(src, dest):
    src = get_point(src)
    dest = get_point(dest)

    parity = ((src[0]+src[1])-(dest[0]+dest[1]))%2 #0 even modes, 1 odd moves

    d = dist(src,dest)

    if d%KNIGHT==0:
        m = d//KNIGHT
    else:
        m = d//KNIGHT+1

    if m%2!=parity:
        moves = m+1
    else:
        moves = m
    
    return moves


