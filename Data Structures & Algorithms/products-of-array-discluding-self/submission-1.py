class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = right = 1

        for i in range(n):
            res[i] *= left
            left *= nums[i]

        for i in range(n)[::-1]:
            res[i] *= right
            right *= nums[i]

        return res
        
"""
prefix and suffix products:
- initialize a res list to store the prefix products, and
final result with size [1] * n where n -> len(nums)
- initialize a left and right variable to track the prefix
and suffix products respectively and assign a value of 1
- iterate over the range of n, assign the product of the
element at the current index in res and the current value
of left to that element
- increment left by the product of the current left and
the current element at the current index in nums
- repeat this process for right but with a reverse copy
of nums range -> [::-1]
- return res

"""