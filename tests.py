import DLalgorithm
import time
import timeit

print ("\ntests.py\n")
print ("Now testing speed of hash table, trie, and directed acyclic word graph dictionaries.")


print ("Now testing hash table...")
start = timeit.default_timer()
d = DLalgorithm.dl_algorithm("words.txt",1)
print ("\nTime taken to construct hash table dictionary: " + str(timeit.default_timer() - start))

print ("Input: 'the', output: " + d.correct('the') + ". Time taken: " + str(timeit.default_timer() - start))
print ("You should be seeing 'the' above.")
print ("Input: 'drangus', output: " + d.correct('drangus') + ". Time taken: " + str(timeit.default_timer() - start))
print ("You should be seeing 'ranges' above.")
print ("Input: '', output: " + d.correct('') + ". Time taken: " + str(timeit.default_timer() - start))
print ("You should be seeing 'a' above.")
print ("Input: 'asdfghj', output: " + d.correct('asdfghj') + ". Time taken: " + str(timeit.default_timer() - start))
print ("You should be seeing 'No similar word found' above. If a word has no relatively close matches the autocorrect implementation will just return nothing at all. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")


print ("Now testing trie...")
start2 = timeit.defualt_timer()
d2 = DLalgorithm.dl_algorithm("words.txt", 2)
print ("\nTime taken to construct trie dictionary: " + str(timeit.default_timer() - start2))

print ("Input: 'the', output: " + d2.correct('the') + ". Time taken: " + str(timeit.default_timer() - start2))
print ("You should be seeing 'the' above.")
print ("Input: 'drangus', output: " + d2.correct('drangus') + ". Time taken: " + str(timeit.default_timer() - start2))
print ("You should be seeing 'ranges' above.")
print ("Input: '', output: " + d2.correct('') + ". Time taken: " + str(timeit.default_timer() - start2))
print ("You shoudl be seeing 'a' above.")
print ("Input: 'asdfghj', output: " + d2.correct('asdfghj') + ". Time taken: " + str(timeit.default_timer() - start2))
print ("You should be seeing 'No similar word found' above. If a word has no relatively close matches the autocorrect implementation will just return nothing at all. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")


print ("Now testing D.A.W.G...")
start3 = timeit.defualt_timer()
d3 = DLalgorithm.dl_algorithm("words.txt", 3)
print ("\nTime taken to construct trie dictionary: " + str(timeit.default_timer() - start3))

print ("Input: 'the', output: " + d3.correct('the') + ". Time taken: " + str(timeit.default_timer() - start3))
print ("You should be seeing 'the' above.")
print ("Input: 'drangus', output: " + d3.correct('drangus') + ". Time taken: " + str(timeit.default_timer() - start3))
print ("You should be seeing 'ranges' above.")
print ("Input: '', output: " + d3.correct('') + ". Time taken: " + str(timeit.default_timer() - start3))
print ("You shoudl be seeing 'a' above.")
print ("Input: 'asdfghj', output: " + d3.correct('asdfghj') + ". Time taken: " + str(timeit.default_timer() - start3))
print ("You should be seeing 'No similar word found' above. If a word has no relatively close matches the autocorrect implementation will just return nothing at all. It took " + str(stop-start) + " seconds for our program to find the best match for the input.")
