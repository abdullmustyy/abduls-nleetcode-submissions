class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())

"""
hash table:
- initialise a res variable with list defaultdict value
- iterate over strs, for each s initialise a count variable
with a list of size [0] * 26 (letters in the alphabet)
- iterate over s, for each c, get the difference of the ASCII
number of c and that of "a" (lowest in the alphabet), this gives
us the index of c in count list, increment the value at that
index by 1
- using a tuple of count as key, append s to its list in the res
hash table (can't use lists as keys since they are mutable)
- return a list of res values

"""