## Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

def square(x):
    """
    Returns the square of a number.
    """
    return x**2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(square, numbers))

print(squares)