f = open('words/words.txt', 'r');

def make_trie():
  root = dict()
  for line in f:
    truncate_line = line(0:(len(line)-1))
    current_dict = root
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict = current_dict.setdefault(_end, _end)
  return root