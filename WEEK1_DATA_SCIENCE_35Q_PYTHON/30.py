## The Fibonacci Sequence is computed based on the following formula: f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1. Please write a program to compute the value of f(n) with a given n input by console.
## Example: If the following n is given as input to the program:7 
## Then, the output of the program should be: 13 
## In case of input data being supplied to the question, it should be assumed to be a console input.

n = int(input("Enter a number: "))

# initialize the first two numbers in the sequence
fib1, fib2 = 0, 1

# compute the nth Fibonacci number
for i in range(2, n+1):
    fib_n = fib1 + fib2
    fib1 = fib2
    fib2 = fib_n

# print the result
print(fib_n)

