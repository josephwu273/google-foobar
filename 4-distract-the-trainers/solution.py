#Ran into a bunch of stupid problems because foobar inexplicably uses Python 2


#from math import gcd

def diverge(x,y):
    n = x+y
    nn = n
    while nn>>1==nn/2.:
        nn = nn>>1
    #f = (x+y)//gcd(x,y)
    return x%nn


def solution(banana_list):
    guards = {i:set() for i in range(len(banana_list))}
    for i,v in enumerate(banana_list):
        for j,vv in enumerate(banana_list):
            if diverge(v,vv):
                guards[i].add(j)
                guards[j].add(i)
    partner_number = {i:len(guards[i]) for i in guards}
    no_friends = 0
    while guards:
        least_friends = min(partner_number, key=partner_number.get)
        if partner_number[least_friends]==0:
            no_friends += 1
            guards.pop(least_friends)
            partner_number.pop(least_friends)
            continue
    
        lf_partner = min(guards[least_friends], key = lambda x: partner_number[x])
        for f in guards[lf_partner]:
            guards[f].remove(lf_partner)
            partner_number[f] -= 1
        for f in guards[least_friends]:
            guards[f].remove(least_friends)
            partner_number[f] -= 1
        
        guards.pop(least_friends)
        guards.pop(lf_partner)
        partner_number.pop(least_friends)
        partner_number.pop(lf_partner)
    return no_friends