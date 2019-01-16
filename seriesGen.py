def seriesGen(numstr, nser):
    sList = []
    for idx in range(len(numstr) - nser + 1):
        sList.append(numstr[idx:idx+nser])
    return sList
    
print(seriesGen("49142", 3))