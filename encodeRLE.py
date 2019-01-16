def encodeRLE(werd):
    curr = ''
    cnt = 0
    enc = []
    for ch in werd:
        if ch != curr:
            enc.append(str(cnt) + curr) if cnt>1 else enc.append(curr)
            curr = ch
            cnt = 1
        else:
            cnt+=1
    enc.append(str(cnt) + curr) if cnt>1 else enc.append(curr)
    return ''.join(enc)

def decodeRLE(werd):
    tmpList = []
    finList = []
    for ch in werd:
        if ch.isnumeric():
            tmpList.append(ch)
        else:
            finList.append(ch*int(''.join(tmpList))) if tmpList else finList.append(ch)
            tmpList = []
    return ''.join(finList)

# testr = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
testr = '  hsqq qww  '
print(encodeRLE(testr))
print(decodeRLE(encodeRLE(testr)))
print(decodeRLE(encodeRLE(testr)) == testr)