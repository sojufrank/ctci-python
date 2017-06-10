#3.S Sort Stack

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None
        
    def set(self, pointer):
        self.next = pointer

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
        n = self.head.value
        self.head = self.head.next
        return n

    def listPrint(self):
        print('start')
        current = self.head
        while current:
            print(current.value)
            current = current.next
        print('end\n')

    def peek(self):
        return self.head.value

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
test = linkedList()
arr = [1,1,1,3,5,7,1,9,2,8,6,8,2,4,1,1,1]

for i in arr:
    test.push(i)

def sort(s):
    r = linkedList()
    while s.isEmpty() == False:
        temp = s.pop()
        while r.isEmpty() == False and temp < r.peek():
            s.push(r.pop())
        r.push(temp)
    while r.isEmpty() == False:
        s.push(r.pop())

test.listPrint()  
sort(test)
test.listPrint()
