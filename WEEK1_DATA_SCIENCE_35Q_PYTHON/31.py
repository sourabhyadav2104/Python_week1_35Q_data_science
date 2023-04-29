## Write a program to compute: f(n)=f(n-1)+100 when n>0 and f(0)=0 with a given n input by console (n>0). 
## Example: If the following n is given as input to the program:5 
## Then, the output of the program should be:500 In case of input data being supplied to the question, it should be assumed to be a console input.

n = int(input("Enter a number greater than zero: "))

# initialize the first value in the sequence
f_n = 0

# compute the nth value in the sequence
for i in range(1, n+1):
    f_n = f_n + 100

# print the result
print(f_n)
