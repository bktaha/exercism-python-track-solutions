def isArmstrong(num):
    cheatDgt = str(num)
    numDgt = len(cheatDgt)
    sumSq = 0
    for dgt in cheatDgt:
        sumSq += int(dgt)**numDgt
    return num == sumSq
    
print(isArmstrong(9))