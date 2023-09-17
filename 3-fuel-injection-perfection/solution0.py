"""
Uses a Djikstra-like approach. Not fast enough!
"""
def neighbors(x):
    if x==1:
        return {2}
    if x%2==0:
        return {x-1,x+1,x//2,2*x}
    else:
        return {x-1,x+1,2*x}

def solution(n):
    n = int(n)
    dists = {1:0}
    layer = 0
    while n not in dists:
        frontier = set()
        for x in dists:
            frontier = frontier.union(neighbors(x))
        for f in frontier:
            if f not in dists:
                dists[f] = layer+1
        layer += 1
        print(dists)
    return dists[n]
