class Solution:
    def isalphanum(self, c: str) -> bool:
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if self.isalphanum(c))
        l, r = 0, len(s) -1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
