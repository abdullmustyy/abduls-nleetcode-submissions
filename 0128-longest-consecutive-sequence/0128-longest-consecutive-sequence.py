class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0

        for n in store:
            if n - 1 not in store:
                streak = 1
                curr = n

                while curr + 1 in store:
                    streak += 1
                    curr += 1

                res = max(res, streak)

        return res

"""
hash table:
- initialise a res variable to track the count of sequences
found, and a store variable, a hash set of nums
- iterate over nums, where num - 1 not in store, set a sreak
and curr variable initialised to 1 and num respectively
- if curr + 1 in store, increment streak and curr by 1
- update res with the maximum between res and streak
- return res

"""