"""
Problem: Valid Parentheses

Description:
Given a string containing the characters (), [], and {}, determine whether the parentheses are valid.

A string is valid if:

- Every opening bracket has a corresponding closing bracket of the same type.
- Brackets are closed in the correct order.
- Every closing bracket has a corresponding opening bracket.

Examples:
Input: ["([{}])"]
Output: True

Complexity:
Time: O(n)
Space: O(n)
"""

def valid_parentheses(cadena):

    stack = []

    pares = {
    ")": "(",
    "]": "[",
    "}": "{"
    }

    for caracter in cadena:
        if caracter in "({[":
            stack.append(caracter)

        if caracter in ")}]":
            if not stack:
                return False
            else:
                ultimo = stack.pop()


            if ultimo == pares[caracter]:
                continue
            return False

    if not stack:
        return True
    return False

print(valid_parentheses("([{}])"))