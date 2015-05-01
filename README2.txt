To compile/run our code, run Python in the terminal window:

$ python

Import our code:

>>> from DLalgorithm import *

Now create an instance of the DLalgorithm corrector. It takes two arguments, the first being
  the name of the dictionary to be used and the second being the type of storage structure to be used: 1 for hash table, 2 for trie, and 3 for directed acyclic word graph:

>>> corrector = dl_algorithm('words.txt', 1)

To correct a word, use the correct method of the algorithm and pass it the string to be corrected:

>>> corrector.correct('word')