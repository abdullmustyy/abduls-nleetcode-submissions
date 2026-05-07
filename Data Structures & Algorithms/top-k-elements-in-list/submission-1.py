class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}
        res = []

        for n in nums:
            if n not in f_map:
                f_map[n] = 1
            else:
                f_map[n] += 1

        for _ in range(k):
            f_max = max(f_map.values())

            def isEqualMax(item):
                n, f = item
                return f == f_max

            n, _ = list(filter(isEqualMax, f_map.items()))[0]

            res.append(n)
            f_map.pop(n)

        return res

"""
brute force, hash map:
- declare a hash map (f_map) to track the frequency of the integers,
and a res array to store the top k frequent elements
- iterate over nums, if current int (n) not in f_map, add it to the
map with a frequency value of 1
- else, increment the frequency
- iterate over the range of k, find the max of f_map values, append
it to the res array, then remove its value and its key from f_map
- return res

"""