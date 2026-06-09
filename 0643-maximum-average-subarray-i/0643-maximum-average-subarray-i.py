class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        ans = s = sum(nums[:k])

        for right in range(k, len(nums)):
            s += nums[right] - nums[left]
            ans = max(ans, s)
            left += 1

        return ans / k