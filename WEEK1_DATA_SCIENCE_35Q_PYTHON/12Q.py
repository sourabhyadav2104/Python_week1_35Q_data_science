## Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

while True:
    try:
        # Accept a sentence from the user
        sentence = input("Enter a sentence (enter 'quit' to exit): ")
        
        # Exit the loop if the user enters "quit"
        if sentence == "quit":
            break
        
        # Check if the sentence contains any letters
        if not any(char.isalpha() for char in sentence):
            print("Warning: The sentence you entered does not contain any letters.")
        
        # Initialize counters for upper case letters and lower case letters
        num_upper = 0
        num_lower = 0
        
        # Loop through each character in the sentence
        for char in sentence:
            # Check if the character is upper case or lower case and increment the corresponding counter
            if char.isupper():
                num_upper += 1
            elif char.islower():
                num_lower += 1
        
        # Print the number of upper case and lower case letters in the sentence
        print(f"Number of upper case letters: {num_upper}")
        print(f"Number of lower case letters: {num_lower}")
    except TypeError:
        print("Invalid input. Please enter a valid sentence.")
