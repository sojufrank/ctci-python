#2.S Sum Lists

class linkedList:
    def __init__(self):
        self.head = None
        self.length = 0

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
        self.length += 1

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('length: ',self.length,'\n')

l1 = linkedList()
l2 = linkedList()

input1 = [7,1,6]
input2 = [5,9,2]

for i in input1:
    l1.insert(i)
for i in input2:
    l2.insert(i)

l1.listPrint()
l2.listPrint()

def sumLists(list1, list2):
    if list1.length != list2.length:
        print('list lenghs do not match')
        return

    p1 = list1.head
    p2 = list2.head
    a1 = []
    a2 = []

    while p1 != None:
        print(p1.value,p2.value)
        a1.append(str(p1.value))
        a2.append(str(p2.value))
        p1 = p1.next
        p2 = p2.next

    n1 = ''
    n2 = ''
    for i in a1:
        n1 += i
    for i in a2:
        n2 += i
    
    n = int(n1)+int(n2)
    n = str(n)

    l3 = linkedList()
    
    for i in n:
        l3.insert(i)
    l3.listPrint()

    
sumLists(l1,l2)
