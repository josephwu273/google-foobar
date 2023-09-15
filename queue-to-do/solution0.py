# Nifty, but ultimately not fast enough
from functools import reduce

def solution(start, length):
    ids = []
    f = start
    for i in range(length):
        ids.extend(range(f, f+length-i))
        f += length
    return reduce(lambda x,y: x^y, ids)