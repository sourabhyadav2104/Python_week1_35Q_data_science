## Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_numbers = tuple(num for num in original_tuple if num % 2 == 0)

print(even_numbers)
