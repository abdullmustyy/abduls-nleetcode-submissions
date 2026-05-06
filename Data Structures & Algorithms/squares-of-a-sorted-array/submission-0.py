class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        res = []

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
- define a left, right, pointer variables, and a result
array
- while the left pointer is less than the right pointer,
if the value at the current left point is less that the right,
add the value at the right point to the result array then
decrease the right pointer, else, do the opposite
- reverse the array because it will be sorted decreasingly
- return result

"""