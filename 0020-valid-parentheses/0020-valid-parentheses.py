class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pValid = {"{}", "()", "[]"}
        openPs = "{(["

        for c in s:
            if c in openPs:
                stack.append(c)
            elif not stack or stack.pop() + c not in pValid:
                return False

        return not stack

"""
stack:
- initialise a stack variable
- initialise a valid parenthesis map to store
valid parenthesis combination
- for c in s
    - if c in "({[" append it to the stack
    - else if not stack, stack.pop() + c not in
    the valid map, return false
- return not stack

"""