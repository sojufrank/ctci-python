#doubly linked list queue

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def pop(self):
        current = self.tail
        self.tail = self.tail.prev
        print(current.value, 'has been popped\n')
        return current

    def listPrint(self):
        print('start print list')
        current = self.tail
        while current != None:
            print(current.value)
            current = current.prev
        print('end print list\n')

test = linkedList()
for i in range(10):
    test.push(i)
test.listPrint()
test.pop()
test.listPrint()
