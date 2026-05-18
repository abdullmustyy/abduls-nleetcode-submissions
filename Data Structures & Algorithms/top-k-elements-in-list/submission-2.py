class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map, nums_items, res = {}, [], []

        for n in nums:
            nums_map[n] = nums_map.get(n, 0) + 1

        for num, freq in nums_map.items():
            nums_items.append([freq, num])

        nums_items.sort()

        for _ in range(k):
            res.append(nums_items.pop()[1])

        return res

"""
sorting:
- initialize an num_map, nums_items, and res variable to store the
hash table of the elements and their frequencies, list of the hash
table's items, and the result list respectively
- iterate over nums to compute the element and frequency map
- iterate over nums_map to compute its items list in [[freq, num]]
order
- sort nums_items
while len(res) < k pop the last element from nums_items and append
its last element to res
- return res

"""