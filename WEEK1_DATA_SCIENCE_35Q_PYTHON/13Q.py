## Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

while True:
    try:
        num_list = input("Enter a list of comma-separated numbers: ")
        num_list = [int(num) for num in num_list.split(",")]
        odd_squares = [num**2 for num in num_list if num % 2 != 0]
        print("The squares of the odd numbers in the list are:", odd_squares)
        break
    except ValueError:
        print("Invalid input. Please enter a list of comma-separated integers.")
