# Create individual node class
class Node:
    def __init__(self, data, ):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def removeItem(self, n):
        # Empty list case
        if self.head == None:
            return
        # Remove first item case
        if n == 0:
            self.head = self.head.next
            return
        # normal case
        currentItem = self.head
        for item in range(n-1):
            currentItem = currentItem.next
        currentItem.next = currentItem.next.next

    def printList(self):
        tempHead = self.head
        while (tempHead != None):
            print(tempHead.data, end="--->")
            tempHead = tempHead.next
        print()


LL = LinkedList()

# Prep nodes
n1 = Node("Peter")
n2 = Node("Harry")
n3 = Node("Ann")
n4 = Node("Ria")

# Construct LinkedList
LL.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

# Remove given item from LL
LL.printList()
LL.removeItem(1)
LL.printList()
