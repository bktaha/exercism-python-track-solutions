def wordCounts(inpstr):
    allwords = inpstr.split(" ")
    wordset = set(allwords)
    counts = {}
    for werd in wordset:
        counts[werd] = allwords.count(werd)
    return counts
    
inpstr = input("Counts Drakula: ")
print(wordCounts(inpstr))