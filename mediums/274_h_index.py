# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their ith paper, return the researcher's
# h-index.

# According to the definition of h-index on Wikipedia: The h-index is defined
# as the maximum value of h such that the given researcher has published at
# least h papers that have each been cited at least h times.

# 0 <= citations[i] <= 5000

# Example 1:
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and
# each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.

# Example 2:
# Input: citations = [1,3,1]
# Output: 1

# Example 3:
# Input: citations = [1]
# Output: 1
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        # [0, 1, 3, 5, 6]
        citations_length = len(citations)
        # You need the hIndex for 0 as an initializer - all the elements are
        # greater than or equal to 0 according to the constraints
        hIndex = len(hIndex)
        for i in range(citations_length):
            # 1 article with at least 1 citation, 2 with 2 and so on...
            # So, go through the array till you reach a number greater than i
            ptr = 0
            while citations[ptr] < i:  # You want to stop at 3 so < not <=
                ptr += 1  # Sorting allows you to do this
            # Only change hIndex if it actually satisfies the condition
            hIndex = i if i <= citations_length - ptr else hIndex

        return hIndex

solution = Solution()
print(solution.hIndex([1]))
# assert solution.hIndex([3,0,6,1,5]) == 3
# assert solution.hIndex([1,3,1]) == 1