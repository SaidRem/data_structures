# Binary Search Trees
# Time complexity for search, insert, delete: O(log n)


class Node:
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
