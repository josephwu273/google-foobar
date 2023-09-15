from functools import reduce

def solution(start, length):
    """
    This solution relies on several XOR facts
    1) For even number e, e^e+1=1
    2) 1^1=0
    3) x^0=x
    """
    simplified_xor = []
    s = start
    for i in range(length):
        q = length-i
        f = s+q-1
        pairs = q//2
        if s%2==1 and q%2==0:
            #o(eo....eo)e
            simplified_xor.append(s)
            simplified_xor.append(f)
            pairs = (q-2)//2
        elif s%2==1 and q%2==1:
            #o(eo...eo)
            simplified_xor.append(s)
        elif s%2==0 and q%2==1:
            #(eo...eo)e
            simplified_xor.append(f)
        else: #s%2==0 and q%2==0
            #(eo...eo)
            pass
        simplified_xor.append(pairs%2)
        s += length
    return reduce(lambda x,y: x^y, simplified_xor)