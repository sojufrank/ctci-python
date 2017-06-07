#2.8 Loop Detection

class Circle:
    circlePointer = None

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def setCirclePointer(self, i):
        current = self.head
        while current != None:
            if current.value == i:
                Circle.circlePointer = current
            current = current.next

    def linkCircle(self):
        current = self.head
        while current != None:
            if current.next == None:
                current.next = Circle.circlePointer
                return
            current = current.next

    def  listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next

    def colide(self):
        slow = self.head
        fast = self.head

        while slow:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print('found collision')
                break

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast

        

test = linkedList()
arr = range(1,100)
for i in arr:
    test.insert(i)

test.setCirclePointer(50)
test.linkCircle()
#test.listPrint()
result = test.colide()
print(result.value)
