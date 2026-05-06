class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, res = 0, len(nums) - 1, []

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[r] ** 2)
                r -= 1
            else:
                res.append(nums[l] ** 2)
                l += 1

        res.reverse()
        return res

"""
two pointers:
- initialize variables for a left pointer (l), right pointer (r),
and result array (res)
- while l is less than or equal to r
- if the absolute value at l is less than the one at r, append
the square of the value at r to res, then decrease r
- else, do the opposite
- this approach will sort res decreasingly, so return reversed res 

"""