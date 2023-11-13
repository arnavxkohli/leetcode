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

# O(nlogn) solution:
# To compute the researcher's h-index, we can sort the citations array in
# non-increasing order and then iterate through the sorted array. For each
# citation count, we compare it to the number of papers that have at least
# that many citations, which can be calculated as the remaining elements in
# the array. If the citation count is greater than or equal to the number of
# papers with at least that many citations, we have found the h-index.

# For example, given the citations array [3,0,6,1,5], we can sort it to obtain
# [6,5,3,1,0]. We then iterate through the sorted array and for each citation
# count, we compare it to the number of remaining elements in the array. For
# the first element, 6, there are 5 remaining elements in the array, all of
# which have at least 6 citations, so the h-index is 6. For the second
# element, 5, there are 4 remaining elements in the array, all of which have
# at least 5 citations, so the h-index is 5. For the third element, 3, there
# are 3 remaining elements in the array that have at least 3 citations, so the
# h-index is 3.

# Time Complexity: O(nlogn), where n is the length of the citations array.
# This is because we need to sort the array in non-increasing order, which
# takes O(nlogn) time.

# Space Complexity: O(1), as we are sorting the array in-place and using only
# constant extra space.

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) # Sort the array in non-increasing order
        citations_length = len(citations)
        hIndex = 0

        # Iterate through the sorted array and compare each citation count to
        # the number of papers that have at least that many citations
        for index, element in enumerate(citations):
            if element >= index+1:
                # If the citation count is greater than or equal to the number
                # of papers with at least that many citations, we have found
                # the h-index
                hIndex = index+1

        return hIndex


solution = Solution()
assert solution.hIndex([3,0,6,1,5]) == 3
assert solution.hIndex([1,3,1]) == 1
assert solution.hIndex([1]) == 1
assert solution.hIndex([0]) == 0