class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        for _ in range(n):
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]

"""
two pointers:
- set a pointer l to the left of numbers and a r to the right
- iterate over the range of len(numbers)
- if the addition of the numbers at bothe pointers, is greater
than target, decrease r, if less than increase l, if equal
return the list of the increment of l and r by one

"""