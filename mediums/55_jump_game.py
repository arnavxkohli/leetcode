# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Smart, intuitive solution
        '''
        # Only the first index is reachable now
        reachable = 0
        # max_jump is the maximum jump you can undertake from the index you
        # are at
        for index, max_jump in enumerate(nums):
            # If you are at an index in the array which isn't reachable,
            # It is impossible to reach the end of the array
            # Obviously if you cross the last index then it's fine
            if index > reachable:
                return False
            # Update the maximum reachable index at the moment.
            reachable = max(reachable, index + max_jump)

        return True

    def canJumpDP(self, nums: List[int], memo = None) -> bool:
        '''
        Works, but very bad performance. This is the brute force and not so
        smart solution to the problem.
        '''
        if memo is None:
            memo = {}
        if len(nums) < 2:
            return True
        if nums[0] == 0:
            return False
        elif nums[0] >= len(nums) - 1:
            return True

        if tuple(nums) not in memo:
            jump_possible = False
            for jump in range(1, nums[0] + 1):
                jump_possible = self.canJumpDP(nums[jump:], memo)
                if jump_possible:
                    break
            memo[tuple(nums)] = jump_possible

        return memo[tuple(nums)]


solution = Solution()
print(solution.canJump([3,2,1,0,4]) == solution.canJumpDP([3,2,1,0,4]))