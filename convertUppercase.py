# accept a list of strings and return a new list with all strings converted to uppercase

def uppercase(words):
    return [word.upper() for word in words]    

num = int(input("Enter the size of your list:"))
words = list()

for i in range(num):
    words.append(input(f"Enter any word {i+1}:"))
    
upper_case = uppercase(words)

print(f"The uppercse of the list is: {upper_case}")