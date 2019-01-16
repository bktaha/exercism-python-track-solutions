def sumMult(num, nList):
    allsets = []
    for cdd in nList:
        uBound = num // cdd if num % cdd else (num // cdd) - 1
        nset = {cdd*rn for rn in range(1, uBound+1)}
        allsets.append(nset)
    print(allsets)
    fset = allsets[0]
    for mset in allsets[1:]:
        fset = fset | mset
    return sum(list(fset))
    
print(sumMult(20, [3,5]))