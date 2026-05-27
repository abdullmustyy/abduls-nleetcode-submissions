class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_set = {}
        t_set = {}

        for char in s:
            freq = s_set.get(char, 0)
            s_set[char] = freq + 1

        for char in t:
            freq = t_set.get(char, 0)
            t_set[char] = freq + 1

        for key in s_set:
            if s_set.get(key) != t_set.get(key):
                return False

        return True