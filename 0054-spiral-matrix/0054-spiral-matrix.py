class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        while matrix:
            res += matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            if matrix:
                res += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res

"""
- initialize an empty res list
- while matrix, pop the first matrix row and add it to res
- if matrix and the first matrix row, iterate over each row in
matrix, pop the last number and append it to res
- if matrix, pop the last row, create a reverse copy and add it
to res
- if matrix and the first matrix row, create a reverse copy of
matrix, iterate over each of it row(s), pop the first number in
the row and append it to res
return res

"""