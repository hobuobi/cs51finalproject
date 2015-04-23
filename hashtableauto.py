from collections import defaultdict
import re
import random

letters = 'abcdefghijklmnopqrstuvwxyz'

def closest(word):
    splitset = [(word[:x],word[x:]) for x in range(len(word)+1)]
    deleteset = [x+y[1:] for (x,y) in splitset if y]
    transposeset = [x+y[1]+y[0]+y[2:] for (x,y) in splitset if len(y)>1]
    replaceset = [x+z+y[1:] for (x,y) in splitset for z in letters if y]
    insertset = [x+z+y for (x,y) in splitset for z in letters]
    return set(deleteset+transposeset+replaceset+insertset)

def getwords(filename):
    text = file(filename).read()
    words = re.findall('[a-z]+', text.lower())
    return words

def hashtable(words):
    hashed = [[] for x in range(50)]
    for word in words:
        hashed[(random.seed(word)).randint(0,49)].append(word)

    def lookup(word):
        return (word in hashed[(random.seed(word)).randint(0,49)])

def dl_algorithm(filename, structtype):
    if structtype = 1:
        try:
            dict = hashtable(getwords(filename))
        except MethodError:
            print ("The hashtable methods are not working properly... yet. - Larry Zhang, 2015")
    elif structtype = 2:
        try:
            dict = trie(getwords(filename))
        except MethodError:
            print ("The trie methods are not working properly... yet. - Humphrey Obuobi, 2015")
    elif structtype = 3:
        try:
            dict = dawg(getwords(filename))
        except MethodError:
            print ("The D.A.W.G. methods are not working properly... yet. - Ben Zheng, 2015")
    else
        print ("Invalid structtype argument, there are only 3 types of structs currently defined.")
        print ("We currently only have a hashtable, trie, and D.A.W.G. defined.")
        print ("These correspond to arguments 1, 2, and 3. Other arguments are not acceptable.")
        return None;

    print ("ITS WORKING ITS WORKING - Shing-Shing Cao, 2015")

def correct(word, structtype):
    if structtype = 1
        then dict = hashtable(getwords(filename))
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