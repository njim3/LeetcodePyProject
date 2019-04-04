# coding: utf-8


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        oneCount = 0
        adjacentCount = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    oneCount += 1

                    if j < cols - 1 and grid[i][j+1] == 1:
                        adjacentCount += 1

                    if i < rows - 1 and grid[i+1][j] == 1:
                        adjacentCount += 1

        return oneCount * 4 - adjacentCount * 2


if __name__ == '__main__':
    sol = Solution()

    grid = [[0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]]

    print(sol.islandPerimeter(grid))
