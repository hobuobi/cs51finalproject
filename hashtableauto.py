from collections import defaultdict
import re

letters = 'abcdefghijklmnopqrstuvwxyz'

def DLalg(word):
   splitset = [(word[:x],word[x:]) for x in range(len(word)+1)]
   deleteset = [x+y[1:] for (x,y) in splitset if y]
   transposeset = [x+y[1]+y[0]+y[2:] for (x,y) in splitset if len(y)>1]
   replaceset = [x+z+y[1:] for (x,y) in splitset for z in letters if y]
   insertset = [x+z+y for (x,y) in splitset for z in letters]
   return set(deleteset+transposeset+replaceset+insertset)

def correct(word):
    text = file('words.txt').read()
    words = re.findall('[a-z]+', text.lower())
    wordlist = defaultdict(lambda:1)
    for f in words:
        wordlist[f] += 1

    if word in wordlist:
        c1 = [word]
    else:
        c1 = []
    c2 = set(x for x in DLalg(word) if x in wordlist)
    c3 = set(y for x in DLalg(word) for y in DLalg(x) if y in wordlist)
    candidates = c1 or c2 or c3 or [word]
    return max(candidates,key=wordlist.get)

print(correct('dawg'))
print(correct('bollocks'))
print(correct('the'))
