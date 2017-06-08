#stack doubly linked list stack

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None
        self.prev = None
class linkedList:
    def __init__(self):
        self.head = None
        
    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def pop(self):
        current = self.head
        self.head = self.head.next
        self.head.prev = None
        del current

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('\n')


test = linkedList()
arr = range(10)
for i in arr:
    test.push(i)
test.listPrint()
test.pop()
test.pop()
test.listPrint()
test.push(11)
test.listPrint()
