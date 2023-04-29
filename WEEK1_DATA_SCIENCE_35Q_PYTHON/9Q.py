## # prompt user for input and split into binary numbers
input_str = input("Enter comma-separated 4-digit binary numbers: ")
binary_nums = input_str.split(',')

# check if each binary number is divisible by 5
divisible_by_5 = [num for num in binary_nums if int(num, 2) % 5 == 0]

# print the resulting numbers
print(" ".join(divisible_by_5))
