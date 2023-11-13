# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            # Return a tuple with letters of each word sorted in alphabetic
            # order
            key = tuple(sorted(word))
            hash_map[key] = hash_map[key] + [word] if key in hash_map else [word]

        # Exploit built-ins always, they seem to be faster
        return list(hash_map.values())
