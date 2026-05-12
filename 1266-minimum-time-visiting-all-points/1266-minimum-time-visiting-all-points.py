class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0

        for i in range(len(points) - 1):
            x, y = points[i]
            target_x, target_y = points[i + 1]

            ans += max(abs(target_x - x), abs(target_y - y))

        return ans

"""
- create an ans variable and initialize it to 0
- iterate over the range of len(points) - 1
- for each index in the iteration, get the x, y values of the current
coordinates and the target coordinates
- increase the ans variable by the maximum value between the difference
of the target and current coordinates of the x and y value
- then return ans

"""