#2.3 Delete Middle Node
class linkedList:
    def __init__(self):
        self.head = None
        self.searchNode = None

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
        def recursion(pointer):
            if pointer.next == None:
                print(pointer.value)
                return
            else:
                recursion(pointer.next)
                print(pointer.value)
        recursion(current)
        print('\n')

    def search(self, n):
        current = self.head
        while current != None:
            if n == current.value:
                self.searchNode = current
            current = current.next

    def deleteMiddleNode(self):
        if self.searchNode == None or self.searchNode.next == None:
            return 'end of list, '
        node = self.searchNode.next
        self.searchNode.value = node.value
        self.searchNode.next = node.next   

test = linkedList()

for i in range(10):
    test.insert(i)

test.listPrint()

test.search(0)
test.deleteMiddleNode()

test.listPrint()
