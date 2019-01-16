def caesarCipher(msg, variant):
    ciph = []
    for ch in msg:
        nch = ord(ch) + variant - ( 0 if variant + ord(ch) - (ord('a') if ch.islower() else ord('A')) < 26 else 26)
        ciph.append(chr(nch)) if ch.isalpha() else ciph.append(ch)
    return ''.join(ciph)
    
msg1 = "The quick brown fox jumps over the lazy dog."
print(caesarCipher(msg1, 13))

ciph1 = "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
print(caesarCipher(ciph1, 13))