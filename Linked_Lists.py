# A Node insert function has two parameters: a pointer, head,
# pointing to the first node of a linked list, and an integer
# def value that must be added to the end of the list as a new Node object
# Time to access an item in linked list O(n)
# Time to insert an item in linked list O(1)
# Time to delete an item - O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        if head is None:
            head = Node(data)
        elif head.next is None:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)