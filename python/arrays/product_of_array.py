"""
Problem: Product of Array Except Self

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Conditions:
You must solve the problem without using division.
The input array may contain positive, negative, and zero values.
The solution should run in O(n) time.
The output array does not count as extra space for the purpose of space complexity.

Example:

Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Complexity:
Time: O(n)
Space: O(1)

"""

def product_of_array_except_self(nums):

    answer = [1] * len(nums)
    producto_izquierda = 1

    for i in range(len(nums)):
        answer[i] = producto_izquierda
        producto_izquierda *= nums[i]

    producto_der = 1

    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= producto_der
        producto_der *= nums[i]
        
    return answer

print(product_of_array_except_self([1, 2, 3, 4]))