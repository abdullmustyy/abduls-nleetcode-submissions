class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])

                    r -= 1
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

"""
two pointers:
- initialise a res list to store the result
- sort the nums list
- iterate over enumerated nums, for i, and n, initialise
left (l) and right (r) pointers to the next and last element
respectively
- while l < r, add n, mums[l] and nums[r] -> threeSum
- if threeSum greater than 0, decrease r, if less, increase l,
if equal append [n, mums[l], nums[r]] to res
- return res

"""