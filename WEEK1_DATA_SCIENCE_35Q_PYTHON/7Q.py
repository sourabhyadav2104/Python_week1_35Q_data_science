## Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

while True:
    try:
        your_line = input("Enter your line:- ")
        if any (char.isdigit() or char == '.'
            for char in your_line):
            raise ValueError("Please enter a valid string or line of words.")
        your_line.split(' ')
        uppercase_line = your_line.upper()
        print(uppercase_line)
    except ValueError as e:
        print(e)
    break