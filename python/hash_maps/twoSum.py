"""
Problem: Two Sum

Given an array of integers and a target, return the indices
of two numbers that add up to the target.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Complexity:
Time: O(n)
Space: O(n)
"""


def two_sum(numeros, target):

    vistos = {}

    for indice, numero in enumerate (numeros):
        resto = target - numero
        if resto in vistos:
            return vistos[resto], indice 
        else:
            vistos[numero] = indice

print(two_sum([2, 7, 11, 15], 9))