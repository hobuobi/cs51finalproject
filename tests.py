import DLalgorithm
import time
import timeit

print ("DUNDUNDUNDUNDUNDUNDUN *drumroll* *For lack of a better front end*")
time.sleep(2)
print ("First, a demonstration of the Damerau-Levenshtein algorithm applied to hash table data structures.")
time.sleep(2)
print ("We can test a few words (both real and imaginary) to demonstrate the power of our algorithm!")
time.sleep(2)
print ("First, let's try a classic: the word 'the'! Starting algorithm...")
time.sleep(2)
start = timeit.default_timer()
d = DLalgorithm.dl_algorithm("words.txt",1)
print(d.correct("the"))
stop = timeit.default_timer()
print ("The above output should be 'the', and it took " + str(stop-start) + " seconds for our program to construct the hash table structure and check to see the best match for our input among the entries in our vocabulary 'word.txt'!")
time.sleep(4)
print ("Now let's try a longer silly word. 'drangus' seems like a good option! Starting algorithm...")
time.sleep(2)
start = timeit.default_timer()
print(d.correct("drangus"))
stop = timeit.default_timer()
print ("Your should be seeing 'ranges' above. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("Now let's try something more obscure, namely ''. Starting algorithm.")
time.sleep(2)
start = timeit.default_timer()
print(d.correct(""))
stop = timeit.default_timer()
print ("Your should be seeing 'a' above as the algorithm defaults to the first alphabetical entry in our vocabulary. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("As a final test let's try for some actual gibberish: 'asdfghj'. Starting algorithm.")
time.sleep(2)
start = timeit.default_timer()
print(d.correct("asdfghj"))
stop = timeit.default_timer()
print ("Your should be seeing 'No similar word found' above. If a word has no relatively close matches the autocorrect implementation will just return nothing at all. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("Now we're going to run tests for the D-L algorithm applied to trie data structures repeating the tests from above. Though you'll hopefully be seeing the same outputs, take note of the difference in runtimes.")
time.sleep(4)
print ("First, let's try a classic: the word 'the'! Starting algorithm...")
time.sleep(2)
start = timeit.default_timer()
d = DLalgorithm.dl_algorithm("words.txt",2)
print(d.correct("the"))
stop = timeit.default_timer()
print ("The above output should be 'the', and it took " + str(stop-start) + " seconds for our program to construct the hash table structure and check to see the best match for our input among the entries in our vocabulary 'word.txt'!")
time.sleep(4)
print ("Now let's try a longer silly word. 'drangus' seems like a good option! Starting algorithm...")
time.sleep(2)
start = timeit.default_timer()
print(d.correct("drangus"))
stop = timeit.default_timer()
print ("Your should be seeing 'ranges' above. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("Now let's try something more obscure, namely ''. Starting algorithm.")
time.sleep(2)
start = timeit.default_timer()
print(d.correct(""))
stop = timeit.default_timer()
print ("Your should be seeing 'a' above as the algorithm defaults to the first alphabetical entry in our vocabulary. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("As a final test let's try for some actual gibberish: 'asdfghj'. Starting algorithm.")
time.sleep(2)
start = timeit.default_timer()
print(d.correct("asdfghj"))
stop = timeit.default_timer()
print ("Your should be seeing 'No similar word found' above. If a word has no relatively close matches the autocorrect implementation will just return nothing at all. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("Now we're going to run tests for the D-L algorithm applied to DAWG data structures repeating the tests from above. Though you'll hopefully be seeing the same outputs, take note of the difference in runtimes.")
time.sleep(4)
print ("First, let's try a classic: the word 'the'! Starting algorithm...")
time.sleep(2)
start = timeit.default_timer()
d = DLalgorithm.dl_algorithm("words.txt",3)
print(d.correct("the"))
stop = timeit.default_timer()
print ("The above output should be 'the', and it took " + str(stop-start) + " seconds for our program to construct the hash table structure and check to see the best match for our input among the entries in our vocabulary 'word.txt'!")
time.sleep(4)
print ("Now let's try a longer silly word. 'drangus' seems like a good option! Starting algorithm...")
time.sleep(2)
start = timeit.default_timer()
print(d.correct("drangus"))
stop = timeit.default_timer()
print ("Your should be seeing 'ranges' above. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("Now let's try something more obscure, namely ''. Starting algorithm.")
time.sleep(2)
start = timeit.default_timer()
print(d.correct(""))
stop = timeit.default_timer()
print ("Your should be seeing 'a' above as the algorithm defaults to the first alphabetical entry in our vocabulary. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("As a final test let's try for some actual gibberish: 'asdfghj'. Starting algorithm.")
time.sleep(2)
start = timeit.default_timer()
print(d.correct("asdfghj"))
stop = timeit.default_timer()
print ("Your should be seeing 'No similar word found' above. If a word has no relatively close matches the autocorrect implementation will just return nothing at all. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
time.sleep(4)
print ("This concludes the tests section! We hope you've had a good time!")
