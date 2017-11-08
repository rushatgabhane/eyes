words = set(open('words_alpha.txt').read().split())
subwords = {s: s[1:] for s in words if len(s) > 1 and s[1:] in words}
with open('eyes.txt', 'w') as f:
    print(subwords, file=f)
