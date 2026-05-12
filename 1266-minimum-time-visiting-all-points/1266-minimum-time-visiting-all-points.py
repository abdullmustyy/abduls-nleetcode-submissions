class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()

            res += max(abs(x2 - x1), abs(y2 - y1))

            x1, y1 = x2, y2

        return res

"""
- the distance between two points is the maximun value of the
difference between the x and y coordinates
- create a res variable and initialize it to zero
- pop the last point in the points array and make its values
x1 and y1
- while points list still has points in it, pop the current last
point and make that x2 and y1
- increase res by the maximum value of the difference between the
x and y coordinates
- make x1 and y1 values equal x2 and y2
- then return res

"""