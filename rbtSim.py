global deltas
global dirSeq

deltas = {
'E':[1,0],
'S':[-1,0],
'N':[0,1],
'W':[0,-1]
}

dirSeq = ['N', 'E', 'S', 'W']

def elemAdd(pos, delt):
    assert len(pos) == len(delt)
    for idx in range(len(pos)):
        pos[idx] += delt[idx]
    return pos

def rbtSim(coordList, dirFacing, cmdStr):
    for cmd in cmdStr:
        if cmd == 'A':
            coordList = elemAdd(coordList, deltas[dirFacing])
        else:
            newIdx = (dirSeq.index(dirFacing)+1) if cmd == 'R' else (dirSeq.index(dirFacing)-1)
            dirFacing = dirSeq[newIdx%4]
    return [coordList, dirFacing]
    
print(rbtSim([7,3], 'N', "RAALAL"))