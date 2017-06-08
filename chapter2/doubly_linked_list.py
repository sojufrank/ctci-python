#example doubly linked list
class Node:
    def __init__(self,data):
        self.value = data
        self.prev = None
        self.next = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.length += 1
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.length += 1

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def doublePrint(self):
        current = self.head
        while current.next != None:
            print(current.value)
            current = current.next

        while current != None:
            print(current.value)
            current = current.prev

test = doublyLinkedList()
for i in range(10):
    test.insert(i)

#test.listPrint()
test.doublePrint()
