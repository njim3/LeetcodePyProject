# coding: utf-8


# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2

        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1

        topleft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topright = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomleft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomright = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        if all([item.isLeaf for item in
                [topleft, topright, bottomleft, bottomright]]):
            if all([item.val for item in
                    [topleft, topright, bottomleft, bottomright]]) or \
                all([not item.val for item in
                     [topleft, topright, bottomleft, bottomright]]):
                return topleft

        return Node(False, False, topleft, topright, bottomleft, bottomright)
