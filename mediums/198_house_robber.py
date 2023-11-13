# You are a professional robber planning to rob houses along a
# street. Each house has a certain amount of money stashed, the
# only constraint stopping you from robbing each of them is that
# adjacent houses have security systems connected and it will a
# automatically contact the police if two adjacent houses were
# broken into on the same night.

# Given an integer array nums representing the amount of money of
# each house, return the maximum amount of money you can rob tonight
# without alerting the police.

# Example 1
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then
# rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9)
# and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
from typing import List


class Solution:
    def rob(self, nums: List[int], memo=None) -> int:
        """
        At each house, you can either rob it and miss out on the
        previous one, or you can skip it and rob the previous one.
        seems like a counter-intuitive and past thinking approach
        but that's how you convert top-down to bottom-up maybe?
        """
        # Handle the recursion steps
        if len(nums) <= 1:
            return len(nums)

        # Initialization of bottom-up solution
        dp = [0] * len(nums)
        # Set the base cases
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        # DP step
        for i in range(2, len(nums)):
            # To rob or not to rob
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]
        # Interesting to note that the value of this can be the same as dp[-2],
        # depending on if you rob the last house or not


solution = Solution()
assert solution.rob([1, 2, 3, 1]) == 4
assert solution.rob([2, 7, 9, 3, 1]) == 12
