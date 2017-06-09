#3.3 Stack of Plates

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedList:
    limit = 4
    arr = []
    stackN = 0

    def __init__(self):
        self.head = None
        self.stackCounter = 0
        self.test = 0

    def push(self,data):
        node = Node(data)
        last = linkedList.arr[linkedList.stackN]
        if self.head == None:
            if linkedList.stackN > 0:
                last.head = node
                node.next = linkedList.arr[linkedList.stackN-1].head
                last.stackCounter += 1
            else:
                self.head = node
                self.stackCounter += 1
        elif last.stackCounter >= linkedList.limit:
            last.stackCounter = 0
            linkedList.stackN += 1
            newStack = linkedList()
            linkedList.arr.append(newStack)
            newStack.push(data)           
        else:
            node.next = last.head
            last.head = node
            last.stackCounter += 1
        
    def pop(self):
        last = linkedList.arr[linkedList.stackN]
        current = last.head
        last.head = last.head.next
        print(current.value, 'has been removed\n')
        del current

    def popN(self,n):
        current = linkedList.arr[n].head
        try:
            prev = linkedList.arr[n+1].head
            while prev.next != current:
                prev = prev.next
            prev.next = current.next
        except:
            linkedList.arr[n].head = linkedList.arr[n].head.next
        print(current.value, 'has been removed\n')
        del current
        

    def listPrint(self):
        last = linkedList.arr[linkedList.stackN]
        current = last.head
        while current:
            print(current.value)
            current = current.next
        print('\n')

    def segPrint(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
        print('\n')
        
test = linkedList()
linkedList.arr.append(test)
for i in range(10):
    test.push(i)

#test.listPrint()
test.listPrint()
test.popN(2)
test.listPrint()
