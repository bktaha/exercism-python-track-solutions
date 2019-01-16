def diffSq(num):
    sqSum = (num*(num+1)/2)**2
    sumSq = num*(num+1)*(2*num+1)/6
    return sqSum - sumSq
    
print(diffSq(10))