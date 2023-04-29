# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

values = input("Enter the values which you want to add:- ")

# Here values.split(',')method is used for split the values by inserting ',' comma..
my_list = values.split(',')
my_tuple = my_list
print(my_list)
print(my_tuple)