def isEdgeCell(rowidx, colidx, board):
    return True if rowidx ==0 or colidx ==0 or rowidx == len(board)-1 or colidx == len(board[0])-1 else False

def minesweeper(mine):
    rlengths = {len(row) for row in mine}
    assert len(rlengths) == 1
    assert set(''.join(mine)) <= {' ', '*'}
    
    solvedMine = []
    for ridx in range(len(mine)):
        solvedRow = []
        for cidx in range(list(rlengths)[0]):
            minecount = 0
            if mine[ridx][cidx] == '*':
                solvedRow.append('*')
                continue
            for dyidx in [-1,0,1]:
                for dxidx in [-1,0,1]:
                    nridx = ridx + dxidx
                    ncidx = cidx + dyidx
                    try:
                        minecount +=1 if mine[nridx][ncidx] == '*' and nridx >=0 and ncidx >=0 else 0
                    except:
                        pass
            solvedRow.append(str(minecount)) if minecount > 0 else solvedRow.append(' ')
        solvedMine.append(' '.join(solvedRow))
    return solvedMine
    
inp = ["* *",
       "* *",
       "*  "]
print(minesweeper(inp))