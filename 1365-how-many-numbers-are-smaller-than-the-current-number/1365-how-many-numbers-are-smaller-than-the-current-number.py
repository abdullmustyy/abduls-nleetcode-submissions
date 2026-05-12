class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sort = sorted(nums)
        nums_map = {}
        res = []

        for i, v in enumerate(nums_sort):
            if v not in nums_map:
                nums_map[v] = i

        for n in nums:
            res.append(nums_map[n])

        return res

"""
sorting, hash table:
- sort nums and store it in a variable -> nums_sort
- create a hash table to store nums_sort values and indices, then create
an empty res list
- iterate over enumerated nums_sort -> (i, v), if v not in the hash
table, add v to the table with i as its value
- iterate over nums, append the value of every n in the hash table to
the res array and return res

"""