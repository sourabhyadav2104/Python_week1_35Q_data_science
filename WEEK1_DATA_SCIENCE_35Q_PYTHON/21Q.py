## write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

import random

divisible_by_5_and_7 = [num for num in range(10, 151) if num % 5 == 0 and num % 7 == 0]
random_num = random.choice(divisible_by_5_and_7)

print("Random number between 10 and 150 (inclusive) that is divisible by both 5 and 7:")
print(random_num)
