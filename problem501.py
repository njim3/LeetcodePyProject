# coding: utf-8
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counts = defaultdict(int)
        stack = []
        curr = root

        # DFS
        while True:
            while curr:
                stack.append(curr)
                counts[curr.val] += 1
                curr = curr.left

            if len(stack) == 0:
                break

            curr = stack.pop()
            curr = curr.right

        # Find all modes
        mode = -1
        curr_modes = []
        for c in counts:
            if counts[c] == mode:
                curr_modes.append(c)
            if counts[c] > mode:
                mode = counts[c]
                curr_modes = [c]

        return curr_modes
