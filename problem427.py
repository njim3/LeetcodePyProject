# coding: utf-8


class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype Node
        """
        if not grid:
            return None

        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        N = len(grid)

        return Node('*', False,
                    self.construct([rows[:N//2] for rows in grid[:N//2]]),
                    self.construct([rows[N//2:] for rows in grid[:N//2]]),
                    self.construct([rows[:N//2] for rows in grid[N//2:]]),
                    self.construct([rows[N//2:] for rows in grid[N//2:]]))

    def isLeaf(self, grid):
        if not grid:
            return True

        tmpSet = set()

        for row in grid:
            for col in range(len(row)):
                tmpSet.add(row[col])
            if len(tmpSet) > 1:
                return False

        return True


if __name__ == '__main__':
    sol = Solution()

    grid = [[1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]]

    node = sol.construct(grid)

    print(node)
