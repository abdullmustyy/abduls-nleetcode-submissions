class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j, n, m = 0, 0, len(s), len(t)

        while i < n and j < m:
            if s[i] == t[j]:
                j += 1
            i += 1

        return m - j

"""
two pointers:
- start pointer 'i' at the begining of s and 'j' at the
begining of t
- while the pointers are less than the length of their
arrays
- if the values at both pointers match, increase j, then
increase i regardless of this condition
- substract j from the length of t and return its value

"""