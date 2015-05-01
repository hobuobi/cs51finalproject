The main files of our project are DLalgorithms.py, dawg.py, and tests.py. 
Please also run tests.py! Most of the other code in this folder is extraneous
code we wrote along the way to our final code. Through these files, you may 
track our progress, but our final work consists of the two files mentioned 
above. Thank you!

-------------------------------------------------------------------------------

This repository consists of several files, only a few of which are relevant to
our final complete project. Those files are as follows:


DLalgorithm.py
  
  Contains two methods and four classes, three of which implementations of 
  tries, hash tables, and D.A.W.G.s as methods of storing dictionaries, the
  fourth of which is the algorithm itself. Methods are as follows:

  closest
    Takes a word argument and returns a set of possible strings matching
    that word with only one modification. Possible modifications are splitting,
    single letter deletion, adjacent letter swapping, mistyped letter, and
    single letter insertion.

  getwords
    Takes a filename directing towards a dictionary and reads in a list of all 
    the words in that dictionary, returning them as an array.


  Classes are as follows:

  dl_algorithm
    Takes a filename directing towards a dictionary and a number indicating
    the type of data structure the dictionary should be stored as. Returns an
    object which has two methods, an initializer function and a correct
    function which takes in a word and returns a corrected word. 

    This correct function utilizes the lookup function of the data structure to
    check if the word exists in the dictionary; if it does, the word doesn't 
    need to be autocorrected. If it doesn't exist, we generate the set of
    strings similar to that word with only one modification via the global
    getwords function, and iterate through it looking for a string that is in
    the dictionary, a.k.a. an autocorrected version of the word. If none is
    found, we generate the set of strings similar to any string in the set of
    strings similar to the word (a.k.a. two or less modifications) and iterate
    through looking for a string that is in the dictionary, a.k.a. an
    autocorrected version of the word. If no such string is still not found,
    then we give up on the word as being too incorrect (we could keep looking
    but the amount of time taken would be ridiculous).

  trie

    A class implementation of a dictionary as a trie. It has two properties and
    three methods.

    The properties are as follows:
    
    stop
      This acts as an indicator to the end of a word, to be stored in the trie
      at any node where a word terminates.

    t
      This stores the trie dictionary itself. The initializer function modifies
      this and stores the words of the dictionary. The structure of this
      variable is actually nested Python dictionaries.

    The methods are as follows:

    __init__
      Simply initializes the stop and t variables and stores the words of the
      dictionary in the t variable in a trie data structure format.

    lookup
      Takes in a word argument and returns the value returned by lookuphelper
      when passed the t dictionary variable and the word.

    lookuphelper
      Takes in a trie dictionary and a word and returns a Boolean. Operates by
      iterating down the letters of the word and looking for them in the trie
      dictionary. If at any point, the current letter is not in the upper level
      dictionary, we return false. If the end of the word is reached but the
      stop variable is not found in the upper level dictionary, we return false,
      but if the end of the word is reached and the stop variable is found in
      the upper level dictionary, we return true. Otherwise, we move on to the
      next letter and obtain the dictionary value corresponding to the letter
      key in the upper level dictionary, passing both to lookuphelper again.

  hashtable
  
    A class implementation of a dictionary as a hash table. It has a single
    property and two methods.

    The property is as follows:

    hashed
      This acts as the hash table itself, with 50 buckets. The initalizer
      function modifies this and stores the words of the dictionary. The 
      structure of this variable is actually a list of 50 lists.

    The methods are as follows:

    __init__
      Simply initializes the hashed variable and stores the words of the
      dictionary in the hashed variable in a hash table data structure format,
      using the word itself as a seed to a random number generator and taking
      the first number generated mod 50 as the hash.

    lookup
      Takes in a word argument. It calculates the hash of the word using the
      same process as in __init__ and checks if the word is in the list
      corresponding to that hash.

  dawg

    A class implementation of a dictionary as a directed acyclic word graph. It
    simply inherits directly from dawg.py and has two methods.

    The methods are as follows:

    __init__
      Simply initializes the dawg variable and stores the words of the
      dictionary in the dawg variable in a directed acyclic word graph format.

    lookup
      Takes in a word argument. Iterates down the dawg variable checking if the
      word is in the D.A.W.G.

tests.py
  
  Contains the tests we ran on our code in order to test efficiency.



There are other files in here as well, but those are temporary files we created
along the way before incorporating them into our main python file.

-------------------------------------------------------------------------------

To compile/run our code, run Python in the terminal window:

$ python

Import our code:

>>> from DLalgorithm import *

Now create an instance of the DLalgorithm corrector. It takes two arguments, 
the first being the name of the dictionary to be used and the second being the
type of storage structure to be used: 1 for hash table, 2 for trie, and 3 for 
directed acyclic word graph:

>>> corrector = dl_algorithm('words.txt', 1)

To correct a word, use the correct method of the algorithm and pass it the
string to be corrected:

>>> corrector.correct('word')

To test our files, run python on tests.py:

$ python tests.py

