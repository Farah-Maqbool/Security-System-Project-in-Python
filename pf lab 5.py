# Lab5 Question N0: 1
for i in range(100,150+1):
    print(i,end=' ')

# Lab5 Question No: 2
for i in range(50,100+1,2):
    print(i,end=' ')

# Lab5 Question No: 3
for i in range(100+1,150,2):
    print(i,end=' ')

# Lab5 Question No: 4 using while loop
num = int(input("Enter a number:"))
i=1
while i <= 10:
    print(num,"*",i,"=",num*i) 
    i+=1

# Lab5 Question No:4 using for loop 
num = int(input("Enter a number:"))
for i in range(1,10+1):
    print(num,"*",i,"=",num*i)

# Lab5 Question No: 5
a = input("Enter a character:") 
while a != "q":
    print("Done")

# Lab5 Question No:6
num = int(input("Enter a number:"))
factorial = 1
i = 1
while i <= num:
    factorial*=i
    print(f"factorial of {num} is {factorial}")
    i+=1

# Lab5 Question No:7
num = int(input("Enter a number:"))
i = 1
if num <= 0:
    print("Check Number")
else:    
    while i <= num:
        if num % 2 == 0:
            print("Not prime number")
            break
        else:
            print("prime number")
            break

# Lab5 Question No: 8
def print_divisible_numbers(number, limit):
    for i in range(1, limit + 1):
        if i % number == 0:
            print(i)

# Example: Print numbers divisible by 3 up to 20
given_number = 3
upper_limit = 20
print_divisible_numbers(given_number, upper_limit)

# lab5 Question No: 9
def count_odd_even(numbers):
    odd_count = 0
    even_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count

# Get 10 numbers from the user
user_numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(10)]

# Count odd and even numbers
odd, even = count_odd_even(user_numbers)

print(f"Number of odd numbers: {odd}")
print(f"Number of even numbers: {even}")

# Lab5 Question No: 10
def fibonacci_series(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

# Specify the number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Print the Fibonacci series
print(f"Fibonacci series up to {num_terms} terms:")
print(fibonacci_series(num_terms))



           
    


            
        
