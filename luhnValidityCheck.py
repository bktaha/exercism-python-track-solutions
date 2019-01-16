def sumDgt(numstr):
    sumval = 0
    for dgt in numstr:
        sumval += int(dgt)
    print(sumval)
    return sumval

def luhn(ccnum):
    cheatcc = str(ccnum)[::-1]
    newcc = []
    for ctr in range(len(cheatcc)):
        newval = int(cheatcc[ctr])*2
        newval = newval-9 if newval>9 else newval
        newcc.append(str(newval)) if ctr % 2 else newcc.append(cheatcc[ctr])
    print(newcc)
    return not bool(sumDgt(newcc)%10)
    
print(luhn('4539148803436467'))
print(luhn('8275667789865433'))