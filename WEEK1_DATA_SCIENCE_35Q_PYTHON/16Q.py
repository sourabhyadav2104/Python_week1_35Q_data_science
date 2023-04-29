## Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

def print_longest_string():
    """
    Prompts the user for two strings as input and prints the string with maximum length to the console.
    If two strings have the same length, then prints both strings line by line.
    """
    while True:
        try:
            str1 = input("Enter the first string: ")
            str2 = input("Enter the second string: ")
            break
        except:
            print("Invalid input. Please try again.")
    
    len1 = len(str1)
    len2 = len(str2)

    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)
print_longest_string()



