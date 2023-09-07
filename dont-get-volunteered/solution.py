KNIGHT = [
 [0, 3, 2, 3, 2, 3, 4, 5],
 [3, 2, 1, 2, 3, 4, 3, 4],
 [2, 1, 4, 3, 2, 3, 4, 5],
 [3, 2, 3, 2, 3, 4, 3, 4],
 [2, 3, 2, 3, 4, 3, 4, 5],
 [3, 4, 3, 4, 3, 4, 5, 4],
 [4, 3, 4, 3, 4, 5, 4, 5],
 [5, 4, 5, 4, 5, 4, 5, 6]
]

def get_point(n):
    file = n%8
    rank = n//8
    return rank,file

def solution(src, dest):
    src = get_point(src)
    dest = get_point(dest)

    x = abs(src[0]-dest[0])
    y = abs(src[1]-dest[1])
    return KNIGHT[x][y]