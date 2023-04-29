## Write a method which can calculate square value of number!!

def square_of_number():
    while True:
        try:
            number  = int(input("Please enter a number for square:- "))
            return number ** 2
        except ValueError:
            print("Error: Invalid input. Please enter a valid number:- ")

result = square_of_number()
print(result)
