class linkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,data):
            self.value = data
            self.next = None

    def insert(self,data):
        node = linkedList.Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('\n')

    def reverse(self):
        current = self.head

        def recursion(self, pointer, prev):
            if pointer.next == None:
                self.head = pointer
                pointer.next = prev
                return
            else:
                recursion(self, pointer.next, pointer)
                pointer.next = prev
            return pointer.next
        tail = recursion(self, current.next, current)
        tail.next = None
            

test = linkedList()

s = 'hello world'
for c in s:
    test.insert(c)
test.listPrint()
test.reverse()
test.listPrint()
    
