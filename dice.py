def addonetolist(one, l):
    return [one + i for i in l]

def addonelisttomanylists(one, lists):
    temp1 = [i for i in one]
    temp2 = []
    for l in lists:
        for i in l:
            temp2 += addonetolist(i, temp1)
        temp1 = temp2
        temp2 = []
    return temp1
    
def dice(n, s):
    die = [i for i in range(1, s+1)];
    dices = []
    for i in range(n):
        dices.append(die)
        
    return addonelisttomanylists(dices[0],dices[1:])

print(sorted(dice(3,6)))
