class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open = set(("(", "[", "{"))
        close = set((")", "]", "}"))
        charMap = {"(": ")", "[": "]", "{": "}"}
        charStack = []

        for i in range(len(s)):
            if s[i] in open:
                charStack.append(s[i])
            else:
                if charStack:
                    top = charStack.pop()

                    if charMap[top] != s[i]:
                        return False
                else:
                    return False

        return len(charStack) == 0
