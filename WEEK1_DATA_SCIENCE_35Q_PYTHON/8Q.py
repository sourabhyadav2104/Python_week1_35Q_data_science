## Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# Take input from user!!
input_str = input("Enter a sequence of whitespace-separated words: ")

# Split the string into words by using .split()method!!
words = input_str.split()

# Here set()method is used for remove the duplicates from the list and sorted()method is used for sort the string/words!!
unique_words = sorted(set(words))

# The .join()method is used for join the words again into the string by separated with ' ' space!!
print(" ".join(unique_words))
