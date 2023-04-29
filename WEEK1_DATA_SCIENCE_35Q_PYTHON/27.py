## Please write a program which count and print the numbers of each character in a string input by console.
## Example: If the following string is given as input to the program: abcdefgabc 
## Then, the output of the program should be: a,2 c,2 b,2 e,1 d,1 g,1 f,1

input_string = input("Enter a string: ")
char_counts = {}    # a dictionary to store the character counts

for char in input_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

for char, count in char_counts.items():
    print(char + "," + str(count), end=" ")
