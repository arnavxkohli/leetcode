# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Moore's voting Algorithm:
        The intuition behind the Moore's Voting Algorithm is based on the fact
        that if there is a majority element in an array, it will always remain
        in the lead, even after encountering other elements.

        1. The algorithm starts by assuming the first element as the majority
        candidate and sets the count to 1.
        2. As it iterates through the array, it compares each element with the
        candidate:
            a. If the current element matches the candidate, it suggests that
            it reinforces the majority element because it appears again.
            Therefore, the count is incremented by 1.
            b. If the current element is different from the candidate, it
            suggests that there might be an equal number of occurrences of the
            majority element and other elements. Therefore, the count is
            decremented by 1.
                - Note that decrementing the count doesn't change the fact that
                the majority element occurs more than n/2 times.
        3. If the count becomes 0, it means that the current candidate is no
        longer a potential majority element. In this case, a new candidate is
        chosen from the remaining elements.
        4. The algorithm continues this process until it has traversed the
        entire array.
        5. The final value of the candidate variable will hold the majority
        element.
        '''
        # Initialize the candidate arbitrarily
        count = 0
        candidate = 0

        for num in nums:
            # Initialization, and also if you have encountered enough different
            # elements to warrant a new leader. For example if you start with
            # 2 2s, but then reach 2 1s, maybe you should be checking 1 next.
            # Even if the next number is 2 the count will go down to 0 and you
            # will be fine, because candidate will again reset to 2.
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

    def hashMapSolution(self, nums: List[int]) -> int:
        elements = {}
        majority = len(nums)//2

        for element in nums:
            if element not in elements:
                elements[element] = 1
            else:
                elements[element] += 1
                # No need to iterate through hashmap all over again,
                # just check after incrementing the element count if you
                # have found the majority element
                if elements[element] > majority:
                    return element


        # The only way you wouldn't find the majority element in the last way
        # is if it is indeed the last element, and you needed to increment
        # by 1 more to satisfy the comparison.
        return nums[-1]
