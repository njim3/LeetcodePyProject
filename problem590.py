# coding; utf-8


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return

        stack = []
        result = []

        node = root
        done = False

        while not done:
            if node:
                left = None
                if node.children:
                    stack.extend(reversed(node.children))
                    left = stack.pop()

                stack.append(node)
                node = left
            elif stack:
                node = stack.pop()
                if node.children and stack:
                    nextNode = stack.pop()

                    if nextNode in node.children:
                        stack.append(node)
                        node = nextNode
                    else:
                        stack.append(nextNode)
                        result.append(node.val)

                        node = None
                else:
                    result.append(node.val)
                    node = None
            else:
                done = True

        return result