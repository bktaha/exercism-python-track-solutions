def acronymGen(phrase):
    keyt = [parts.split(' ') for parts in phrase.split('-')]
    keyw = [item for sublist in keyt for item in sublist]
    acr = []
    for werd in keyw:
        acr.append(werd[0])
    return ''.join(acr).upper()

print(acronymGen('Complementary metal-oxide semiconductor'))