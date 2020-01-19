# coding: utf-8
# Definition for a Node.


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # iterative
        res = []
        q = [root]

        while q:
            cur = q.pop(0)
            if cur:
                res.append(cur.val)

                q = cur.children + q

        return res
