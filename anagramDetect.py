def charCounts(werd):
    chars = set(werd)
    counts = []
    for ch in chars:
        counts.append(werd.count(ch))
    return counts

def trueAnagrams(werd, falseList):
    trueList = []
    for anag in falseList:
        if len(anag) == len(werd):
            cndd = anag.lower()
            mstr = werd.lower()
            if cndd != mstr and not set(cndd) - set(mstr):
                if charCounts(cndd) == charCounts(mstr):
                    trueList.append(anag)
    return trueList
    
werd = "allergy"
candidates = [
            "gallery", "ballerina", "regally", "clergy", "largely", "leading"
        ]
        
print(trueAnagrams(werd, candidates))