#initializes a set which gets words from words_alpha
words = set(open('words_alpha.txt').read().split())

#another set which gets words only if lenght>1 and the remaining letters form a word that belongs to words_alpha
subwords = {s: s[1:] for s in words if len(s) > 1 and s[1:] in words}

#outputs subwords to a file eyes.txt
with open('eyes.txt', 'w') as f:
    print(subwords, file=f)
