## Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def generate_square_dict():
    """
    Generates a dictionary where the keys are numbers between 1 and 20 (inclusive) and the values are the squares of the keys.
    """
    square_dict = {}
    for i in range(1, 21):
        square_dict[i] = i**2
    return square_dict
my_dict = generate_square_dict()
print(my_dict)
