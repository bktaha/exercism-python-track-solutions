global allergyIndex

allergyIndex = {
'eggs':1,
'peanuts':2,
'shellfish':4,
'strawberries':8,
'tomatoes':16,
'chocolate':32,
'pollen':64,
'cats':128
}

def findAllergies(ascore):
    finList = []
    for allergy in allergyIndex:
        finList.append(allergy) if allergyIndex[allergy] & ascore == allergyIndex[allergy] else None
    return finList
    
print(findAllergies(34))