"""
Problem: Group Anagrams
Description:

Given an array of strings strs, group the anagrams together.

Anagrams are strings that contain the same characters with the same frequencies, regardless of their order.

Return a list of groups, where each group contains strings that are anagrams of each other.

Conditions:
Each string contains lowercase English letters.
The order of the groups does not matter.
The order of the strings within each group does not matter.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

Complexity:
Time: O(k log k)
Space: O(n · k)
"""

def group_anagrams(strs):

    grupos = {}


    for palabra in strs:
        palabra_ordenada = "".join(sorted(palabra))

        if palabra_ordenada in grupos:
            grupos[palabra_ordenada].append(palabra)
        else:
            grupos[palabra_ordenada] = [palabra]

    valores = list(grupos.values())

    return valores

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))