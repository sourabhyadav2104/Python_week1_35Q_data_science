## By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

original_list = [12, 24, 35, 70, 88, 120, 155]
new_list = [original_list[i] for i in range(len(original_list)) if i < 2 or i > 4]

print(new_list)
