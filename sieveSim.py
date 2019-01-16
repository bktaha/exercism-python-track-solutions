def sieveSim(lim):
    fList = list(range(2,lim+1))
    for elem in fList:
        for mult in range(1, lim // elem):
            try:
                fList.remove(elem*(mult+1))
            except:
                continue
    return fList
    
print(sieveSim(23))