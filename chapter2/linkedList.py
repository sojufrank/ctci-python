class linkedlist:
    def __init__(self):
        self.head = None
        
    class Node:
        def __init__(self,data):
            self.value = data
            self.next = None

    def insert(self,data):
        node = linkedlist.Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def listPrint(self):
        current = self.head
        if current == None:
            print('list is empty')
            return
        while current != None:
            print(current.value)
            current = current.next
            
    def reverse(self):
        current = self.head
        if current == None:
            print('list is empty')
            return
        def recursion(self, pointer, prev):
            if pointer.next == None:
                self.head = pointer
                pointer.next = prev
                return
            else:
                recursion(self, pointer.next, pointer)
                pointer.next = prev
            return pointer.next
            
        x = recursion(self, current.next, current)
        x.next = None

test = linkedlist()

s = 'hello world'
for c in s:
    test.insert(c)
test.listPrint()
test.reverse()
print('\n')
test.listPrint()
    
