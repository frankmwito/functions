def remove_duplicates(numbers):
    # Convert the list to a set to remove duplicates
    return list(set(numbers))

# Example usage
num = int(input("Enter the size of your list:"))
numbers = []

for i in range(num):
    numbers.append(int(input(f"Enter number {i+1}:")))

print(f"Original list: {numbers}")
unique_numbers = remove_duplicates(numbers)
print(f"List after removing duplicates: {unique_numbers}")
