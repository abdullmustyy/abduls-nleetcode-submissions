class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_trim = "".join(filter(str.isalnum, s)).lower().replace(" ", "")
        i, j = 0, len(s_trim) - 1

        while i < j:
            if s_trim[i] != s_trim[j]:
                return False

            i += 1
            j -= 1

        return True
        
"""
two pointers:
- initialise a pointer i to the start of the
string and j to its end
-convert s to lowercase
- while i < j, if s[i] != s[j] return false
- increase i and decrese j by one
- otherwise, return true

"""