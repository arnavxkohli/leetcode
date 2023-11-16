# Given an array of strings nums containing n unique binary strings each of
# length n, return a binary string of length n that does not appear in nums.
# If there are multiple answers, you may return any of them.

# Example 1:
# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# Example 2:
# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.

# Example 3:
# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110"
# would also be correct.
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums):
        result = ""

        for i in range(len(nums)):
            # Basically, if you have 111, 011 and 001: at position 0,
            # element 0 you have 1 from 111. Always choose the opposite bit
            # for the result and iterate through the entire array this way.
            # You are guaranteed to find a solution
            result += '1' if nums[i][i] == '0' else '0'

        return result

    def naiveSolution(self, nums: List[str]) -> str:
        ''' O(n^2), not great but this was my own solution '''
        nums_length = len(nums)
        # Convert binary to int, O(n^2) operation because n is length of both
        # array and each array element
        nums = [(sum(int(element) * 2**(nums_length - 1 - i) for i, \
            element in enumerate(nums_element))) \
                for nums_element in nums] # O(n^2)
        # Sort nums, create an array of candidates that you can iterate. The
        # moment candidate is different from a value in num, you have your
        # answer
        nums.sort() # O(nlogn)
        candidates = [i for i in range(2**nums_length)] # O(n)
        # Initialize check through the array
        nums_ptr = 0
        candidates_ptr = 0
        while candidates_ptr < 2**nums_length:
            if nums_ptr >= nums_length or \
                candidates[candidates_ptr] != nums[nums_ptr]:
                # Format and return the binary string
                binary_string = bin(candidates[candidates_ptr])[2:]
                while len(binary_string) < nums_length:
                    binary_string = '0' + binary_string
                return binary_string
            # No need to increment if nums_ptr already at nums_length
            if nums_ptr < nums_length: nums_ptr += 1
            # Always increment
            candidates_ptr += 1


solution = Solution()
solution.findDifferentBinaryString(["111","011","001"])
