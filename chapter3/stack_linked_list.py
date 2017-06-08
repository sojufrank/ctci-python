# stack linked list
class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def pop(self):
        current = self.head
        self.head = self.head.next
        del current

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('\n')

test = linkedList()
for i in range(10):
    test.push(i)
test.listPrint()
test.pop()
test.pop()
test.listPrint()
test.push(42)
test.listPrint()
