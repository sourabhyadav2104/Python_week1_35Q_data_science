## Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# Define an empty list to store the even-digit numbers
even_digit_nums = []

# Loop through each number between 1000 and 3000 (both inclusive)
for num in range(1000, 3001):
    # Convert the number to a string and check if each character is even
    if all(int(digit) % 2 == 0 for digit in str(num)):
        # If all digits are even, add the number to the list
        even_digit_nums.append(str(num))

# Print the even-digit numbers separated by commas on a single line
print(",".join(even_digit_nums))
