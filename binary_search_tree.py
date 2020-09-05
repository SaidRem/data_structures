# Binary Search Tree is a rooted binary tree whose internal
# nodes each store a key greater than all the keys in the node's
# left subtree and less than those in its right subtree.
# Binary search tree support three main operations:
# insertion of elements, deletion of elements and lookup
# - checking whether a key is present.

# Time complexity for search, insert, delete: O(log n)

# Binary search requires an order relation by which every element
# can be compared with every other element in the sense of a total
# preorder.

class Node:
    """create node in binary tree"""
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def level_of_order(self, root):
        pass


n = int(input())
biTree = Solution()
root = None
for i in range(n):
    data = int(input())
    root = biTree.insert(root, data)
