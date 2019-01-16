def hammingDist(dnaseq1, dnaseq2):
    if len(dnaseq1) == len(dnaseq2):
        hamming = 0
        for ctr in range(len(dnaseq1)):
            if dnaseq1[ctr] != dnaseq2[ctr]:
                hamming = hamming+1
        return hamming
    else:
        return None
        
dna1='GAGCCTACTAACGGGAT'
dna2='CATCGTAATGACGGCCT'

print(hammingDist(dna1,dna2))