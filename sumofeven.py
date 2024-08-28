# function that takes a list of numbers as inputs and returns the sum of even numbers in a list

def sum_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if num % 2 == 0:
            sum += num
    return sum

numbers = list()
num = int(input("Enter any number:"))

for i in range(num):
    numbers.append(int(input(f"Enter a number {i+1}:")))

print(f"Your new numbers are: {numbers}")

result = sum_even_numbers(numbers)
print(f"The sum of even numbers is: {result}")