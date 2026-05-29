class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxAmt = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h

            maxAmt = max(maxAmt, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxAmt

"""
two pointers:
- initialise left at the start and right at the end of heights
- initialise maxAmt to store the maximum area found
- while left < right:
    - calculate the width as right - left
    - calculate the height as the smaller of heights[left] and heights[right]
    - calculate the current area
    - update maxAmt
    - move the pointer with the smaller height inward
- return maxAmt

Time: O(n)
Space: O(1)
"""
