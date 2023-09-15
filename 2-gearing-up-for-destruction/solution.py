from fractions import Fraction

def diff(arr):
    return [arr[i]-arr[i-1] for i in range(1,len(arr))]

def checkGear(first, distances):
    current_gear = first
    for d in distances:
        next_gear = d-current_gear
        if next_gear<1 or current_gear<1:
            return False
        else:
            current_gear = next_gear
    return True

def solution(pegs):
    # Your code here1
    d = diff(pegs)
    if len(pegs)%2==0: #is even
        f = Fraction(2,3)
    else:
        f = Fraction(2,1)
    evens = sum(d[0::2])
    odds = sum(d[1::2])
    first_gear = f*(evens-odds)
    if first_gear<1 or not checkGear(first_gear, d):
        return [-1,-1]
    else:
        return [first_gear.numerator,first_gear.denominator]