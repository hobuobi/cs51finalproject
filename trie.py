_stop = 'zz'

def trie(vocab):
	d = dict()
	for word in vocab:
		current = d
		for letter in word:
			current = current.setdefault(letter.lower(), {})
		current = current.setdefault(_stop, _stop)
	return d

_trie1 = trie(open('words.txt'))

def search(t, word):
	"""Returns True if word is in t, false if not
	Precondition t is a trie
	word is a string"""

	letter = word[0:1]
	if (len(word) == 0) and (_stop in t):
		return True
	elif letter in t:
		return True and search(t[letter], word[1:])
	else:
		return False

def lookup(word):
	search(_trie1, word)