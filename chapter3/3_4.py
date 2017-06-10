#3.4 Queue via Stacks

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
            node.next = self.head
            self.head = node

    def pop(self):
        current = self.head
        #print(current.value, 'has beed popped\n')
        self.head = self.head.next
        return current.value

    def listPrint(self):
        print('start list')
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('end list')

class MyQueue:
    def __init__(self):
        self.l1 = linkedList()
        self.l2 = linkedList()

    def push(self,data):
        self.l1.push(data)

    def pop(self):
        current = self.l1.head
        returnNumber = None
        while current != None:
            n = self.l1.pop()
            self.l2.push(n)
            current = current.next
        
        returnNumber = self.l2.pop()
        current2 = self.l2.head
        
        while current2 != None:
            n = self.l2.pop()
            self.l1.push(n)
            current2 = current2.next
            
    def listPrint(self):
        print('list start')
        current = self.l1.head
        while current != None:
            print(current.value)
            current = current.next
        print('list end\n')

test = MyQueue()
for i in range(10):
    test.push(i)
test.listPrint()
test.pop()
test.listPrint()

    
