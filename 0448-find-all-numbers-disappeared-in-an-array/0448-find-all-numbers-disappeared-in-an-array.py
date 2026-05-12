class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        missing_ints = []

        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                missing_ints.append(i)

        return missing_ints

"""
hash map:
- define a missing integer map
- treat the length of the nums list as the benchmark for the
range of the integers to iterate over
- for every integer in range(1, n + 1), where n = len(nums)
- if the integer is not in nums add it to the missing map
- return the missing ints map

"""