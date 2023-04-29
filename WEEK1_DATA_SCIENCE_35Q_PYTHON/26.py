## You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
## If the following string is given as input to the program: 4 bcdef abcdefg bcde bcdef 


input_string = input("Enter string:- ")
words = input_string.split()    # split the string into a list of words
counts = []    # a list to store the counts

for word in words:
    if word not in counts:    # if the word is not counted yet, count it
        counts.append(word)
        print(words.count(word), end=" ")    # output the count



