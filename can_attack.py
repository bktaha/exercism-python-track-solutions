import math

def pointAngle(pos1, pos2):
    arg = (pos2[1]-pos1[1]) / (pos2[0]-pos1[0])
    return math.atan()

def queenAttack(qpos1, qpos2):
    assert qpos1 != qpos2
    assert all(pos >= 0 and pos <=8 for pos in qpos1)
    assert all(pos >= 0 and pos <=8 for pos in qpos2)
    if qpos1[0] == qpos[0] or qpos1[1] == qpos[1] or math.abs(pointAngle(qpos1, qpos2)) == 45:
        return True
    else:
        return False