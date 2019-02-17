# coding: utf-8
import collections

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype List[List[int]]
        """
        result = []
        queue = collections.deque()

        queue.append(root)

        while queue:
            level = []
            queLen = len(queue)

            for _ in range(queLen):
                node = queue.popleft()

                if not node:
                    continue

                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            if level:
                result.append(level)

        return result
