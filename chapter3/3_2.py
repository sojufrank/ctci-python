#3.2 Stack Min

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
        return current

    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.value

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('\n')

class stackMinList(linkedList):
    def push(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            mini.push(node.value)
        else:
            node.next = self.head
            self.head = node
            
        if node.value < mini.peek():
            mini.push(node.value)

    def min(self):
        return mini.peek();
        
mini = linkedList()
test = stackMinList()
arr = [50,30,80,20,90,10,8,22,5,55,1]
for i in arr:
    test.push(i)
    
test.listPrint()
mini.listPrint()

print(test.min())
