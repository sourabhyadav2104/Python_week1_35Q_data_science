# Question:
# Write a program which can compute the factorial of a given numbers.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Enter an number to get the factorial..
n = int(input("Enter a number: "))

# factorial
result = factorial(n)

# Print the variable result which contain the factorial of the given number..
print(result)
