global plain
global cipher

plain =  'abcdefghijklmnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmlkjihgfedcba'

def encAtbash(msg):
    nmsg = ''.join(msg.split(" "))
    ciph = []
    aciph = []
    for ch in nmsg:
        ciph.append(cipher[plain.index(ch)])
    for grps in range(len(ciph) // 5):
        aciph.append(''.join(ciph[grps*5:(grps+1)*5]))
    return ' '.join(aciph)

def decAtbash(ciph):
    nciph = ''.join(ciph.split(" "))
    msg = []
    for ch in nciph:
        msg.append(plain[cipher.index(ch)])
    return ''.join(msg)
    
print(encAtbash('the quick brown fox jumps over the lazy dog'))
print(decAtbash('gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt'))