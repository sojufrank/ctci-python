#2.1 Remove Dups

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

    def remove(self, n):
        current = self.head
        prev = current
        while current != None:
            if n == current.value:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                
            prev = current
            current = current.next

    def removeDuplicate(self):
        i = self.head
        
        while i != None:
            j = i.next
            prev = j
            while j != None:
                if i.value == j.value:
                    if i == self.head:
                        i.next = j.next
                    else:
                        prev.next = j.next
                prev = j
                j = j.next
            i = i.next

ll = linkedList()

#a = [1,3,5,7,9,8,6,4,2]
a = [1,2,6,3,6,4,5,6,7,8,6,9,9]
for i in a:
    ll.insert(i)

ll.listPrint()

ll.removeDuplicate()

ll.listPrint()



    
        
