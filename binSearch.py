def binSrch(can, vals):
    lvals = len(vals)
    if vals == []:
        return -1
    elif can == vals[lvals //2]:
        return lvals //2
    elif can > vals[lvals //2]:
        return binSrch(can, vals[lvals //2:])
    else:
        return binSrch(can, vals[:lvals //2])

def binSearch(nval, ncan, vals, cans):
    inds = []
    for can in cans:
        inds.append(binSrch(can, vals))
    return inds
    
print(binSearch(5,6,[10,20,30,40,50],[40,10,35,15,40,20]))