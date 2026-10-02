"""
Problem: Word Lengths

Description:
Given a string containing multiple words separated by spaces, create a dictionary where each key is a word and its value is the length of that word.

Conditions:
- Each word should be stored as a key in the dictionary.
- The value associated with each word should be its number of characters.
- Words are separated by spaces.
- The solution should also correctly process the last word in the string.

Example:
Input: "Hello World"
Output: {"Hello": 5, "World": 5,}

Complexity:
Time: O(n)
Space: O(n)
"""

def word_lengths(string):
    hash = {}
    word = ""
    count = 0

    for letter in string:
        if letter == " ":
            hash[word] = count
            word = ""
            count = 0
        else:
            word += letter
            count += 1

    hash[word] = count

    return hash

print(word_lengths("Hello World"))