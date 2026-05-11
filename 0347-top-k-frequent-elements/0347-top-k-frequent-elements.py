class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        nums_items = []
        res = []

        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1

        for n, f in nums_map.items():
            nums_items.append([f, n])
        nums_items.sort()

        while len(res) < k:
            res.append(nums_items.pop()[1])
            
        return res