"""
Problem: Contains Duplicate

Description:
Given an integer array nums, determine whether any value appears at least twice in the array.

Return True if any value appears more than once, and False if every element is unique.

Conditions:

The array may contain positive numbers, negative numbers, or 0.
Return True if a duplicate exists.
Return False if all elements are unique.

Example:
Input: [1, 2, 3, 1]
Output: True

Complexity:
Time: O(n)
Space: O(n)
"""

def contains_duplicate(numeros):
    
    numeros_vistos = {}

    for numero in numeros:
        if numero in numeros_vistos:
            return True
        else:
            numeros_vistos[numero] = 1

    return False

print(contains_duplicate([1, 2, 3, 4]))