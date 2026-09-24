"""
Problem: Valid Anagram

Description:
Given two strings s and t, determine whether t is an anagram of s.

An anagram is a word or phrase formed by rearranging all the letters of another word or phrase.

Conditions:
Both strings contain lowercase English letters.
Both strings must contain the same letters with the same frequencies.
The order of the characters does not matter.
Return True if t is an anagram of s; otherwise, return False.

Example:
Input: "anagram", "nagaram"

Output: True
"""

def valid_anagram(s,t):

    contador_s = {}
    contador_t = {}

    for letra in s:
        if letra in contador_s:
            contador_s[letra] += 1
        else:
            contador_s[letra] = 1

    for letra in t:
            if letra in contador_t:
                contador_t[letra] += 1
            else:
                contador_t[letra] = 1

    if contador_s == contador_t:
         return True
    
    return False

print(valid_anagram("anagram", "nagaram"))