## Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

# Taking comma-separated input from user!!
words = input("Enter comma-separated words:- ")

# Split the input into individual words by using words.split()method in my case i separated from ',' !!
words_list = words.split(",")

# The sort()method sorted the list of elements in Alphabatical order!!
words_list.sort()

# .join()method is used here to join the words by ',' !!
sorted_words = ",".join(words_list)

# Print the sorted words!!
print(sorted_words)
