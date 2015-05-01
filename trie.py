_stop = 'zz'

class trie(object):

    def __init__(self, vocab):
	self.t = dict()
	for word in vocab:
		current = self.t
		for letter in word:
			current = current.setdefault(letter.lower(), {})
		current = current.setdefault(_stop, _stop)

    def lookup(self, word):
	"""Returns True if word is in t, false if not
	Precondition t is a trie
	word is a string"""

	letter = word[0:1]
	if (len(word) == 0) and (_stop in self.t):
		return True
	elif letter in self.t:
		return lookup(self.t[letter], word[1:])
	else:
		return False
