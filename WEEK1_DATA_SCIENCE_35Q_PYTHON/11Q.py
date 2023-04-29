## Write a program that accepts a sentence and calculate the number of letters and digits.

# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Initialize counters for letters and digits
num_letters = 0
num_digits = 0

# Loop through each character in the sentence
for char in sentence:
    # Check if the character is a letter or digit and increment the corresponding counter
    if char.isalpha():
        num_letters += 1
    elif char.isdigit():
        num_digits += 1

# Print the number of letters and digits in the sentence
print(f"Number of letters: {num_letters}")
print(f"Number of digits: {num_digits}")
