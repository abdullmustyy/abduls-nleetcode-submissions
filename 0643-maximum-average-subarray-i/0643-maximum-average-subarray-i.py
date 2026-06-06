class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans = s = sum(nums[:k])

        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(ans, s)

        return ans / k
        

"""
sliding window:
- initialize ans and s variable to store initial window sum
- for i in range(k, len(nums))
    - new sum (s) equals old sum (s) + entering element minus
    leaving element
    - ans equals max of current ans and new sum
- return ans / k

"""