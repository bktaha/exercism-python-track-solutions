global brmatch

brmatch = {
    '{':'}',
    '(':')',
    '[':']'
}

def bracketPush(seq):
    tmpSeq = [seq[0]]
    for ch in seq[1:]:
        if ch in list(brmatch) + list(brmatch.values()):
            try:
                tmpSeq.pop() if ch == brmatch[tmpSeq[-1]] else tmpSeq.append(ch)
            except:
                continue
    return not bool(tmpSeq)
    
print(bracketPush('(((185 + 223.85) * 15) - 543)/2'))
print(bracketPush("\\left(\\begin{array}{cc} \\frac{1}{3} & x\\\\ \\mathrm{e}^{"
                 "x} &... x^2 \\end{array}\\right)"))