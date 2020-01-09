# coding: utf-8


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1

        depth = 0
        for node in root.children:
            depth = max(1 + self.maxDepth(node), depth)

        return depth
