# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

try:
    number = int(input("Enter an number:- "))

    my_dictionary = dict()
    for i in range(1,number+1):
        my_dictionary[i] = i*i

        print(my_dictionary) 
except ValueError as ve:
    print("Something went worng..")
    print("Please give an valid number..")
   