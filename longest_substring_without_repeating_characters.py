"""
Problem: Longest Substring Without Repeating Characters

Description:
Given a string s, find the length of the longest substring without repeating characters.

A substring is a contiguous sequence of characters within the string.

Conditions:
0 <= s.length <= 50,000
s may contain letters, digits, symbols, and spaces.
The substring must contain only unique characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc".

Complexity:

"""

def longest_substring_without_repeating_characters(s):

    substring = {}
    contador = 0
    max_substring = 0

    for indice, letra in enumerate(s):
        if not letra in substring:
            substring[letra] = indice
            contador += 1

        else:
            if contador > max_substring:
                max_substring = contador
            
    if contador > max_substring:
        max_substring = contador

    return max_substring

print(longest_substring_without_repeating_characters("abba"))