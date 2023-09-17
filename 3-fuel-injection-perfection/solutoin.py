"""
O(log n) time solution
Easier when you think of input n as a binary string you want to decompose down
to 1
"""
def solution(n):
    n = int(n)
    steps = 0
    while n!=1:
        d0 = bin(n)[-1]
        d1 = bin(n)[-2]
        if d0=='0':
            # 1????0
            #Obvious soln is to divide/bitshift left
            n = n//2
        elif d1=='1' and n!=3:
            n = n+1
            # 1??11
            # If you add 1, you get 1??00, meaning you can do 2 bitshifts in a row
        else:
            # 1??01
            # Subtract 1 to get 1??00, meaning you can do 2 bitshifts in a row
            n = n-1
        steps += 1
    return steps