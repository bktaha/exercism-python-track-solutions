import sys

def validateISBN10(isbn):
    numlist=[]
    for chars in isbn:
        if chars.isnumeric():
            numlist.append(int(chars))
        elif chars == 'X' or chars == 'x':
            numlist.append(10)
    i=10
    msum=0
    while(i):
        msum = msum+numlist[i-1]*(i)
        i = i-1
    return not msum%11
    
print(validateISBN10(sys.argv[1]))