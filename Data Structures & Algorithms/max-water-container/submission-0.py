class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxAmt = 0

        for i in range(n):
            p1, p2 = i, i + 1

            while p2 < n:
                amt = (p2 - p1) * min(heights[p1], heights[p2])
                maxAmt = max(maxAmt, amt)

                p2 += 1

        return maxAmt

"""
two pointers:
- initialise a maxAmt variable to store the max amount
of water
- iterate over heights, initialise p1 and p2 pointers at
the first height and the next
- while p2 < len(heights), current amt equal the difference
of the pointers multiplied by the lower height
- maxAmt equal the higer amount between the current and
max amount

"""
