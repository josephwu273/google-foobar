def solution(x,y):
    x,y = int(x), int(y)
    steps = 0

    while True:
        if x==1 and y==1:
            return str(steps)
        elif x<1 or y<1 or x==y:
            return "impossible"
        else:
            pass
        if x>y:
            d = (x-1)//y
            x -= d*y
            steps += d
        elif y>x:
            d = (y-1)//x
            y -= d*x
            steps += d
        else:
            return "impossible"