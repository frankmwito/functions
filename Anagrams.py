# function that takes two strings as arguments and returns true if the strings are anagrams, otherwise false

def anagrams_check(word1, word2):
    isAnagram = False
    if sorted(word1) == sorted(word2):
        isAnagram = True
    return isAnagram

result = anagrams_check(input("Enter first word: "), input("Enter second word: "))
print(result)