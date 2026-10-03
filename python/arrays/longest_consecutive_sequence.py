"""
Problem: Longest Consecutive Sequence

Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

A consecutive sequence consists of numbers that follow each other without gaps.

Conditions:
The sequence does not need to appear in the same order as the input array.
You must solve the problem in O(n) time.
The array may contain duplicate values.
Return 0 if the array is empty.

Example:
Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].

Complexity:
Time: O(n)
Space: O(1)
"""

def longest_consecutive_sequence(nums):
    
    ordenados = set(nums)
    consecutivos = 0
    max_consecutivos = 0

    if not nums:
        return 0

    for numero in ordenados:
        siguiente = numero + 1
        
        if siguiente in ordenados:
            consecutivos += 1
        else:
            if consecutivos + 1 > max_consecutivos:
                max_consecutivos = consecutivos + 1

            consecutivos = 0
            
    return max_consecutivos
            
print(longest_consecutive_sequence([0, 3, 7, 2, 5, 1, 6, 10, 9, 8]))