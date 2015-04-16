f = open("words.txt", "r");

wordlength = 0;

for line in f:
  if len(line) > wordlength:
    wordlength = len(line);
    print (str(wordlength) + line);