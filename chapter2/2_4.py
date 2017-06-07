#2.4 Partition
# i sailed through this one.  

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

    def partition(self, n):
        current = self.head
        pre = []
        mid = []
        end = []
        final = []

        while current != None:
            if current.value < n:
                pre.append(current.value)
            elif current.value == n:
                mid.append(current.value)
            elif current.value > n:
                end.append(current.value)
            else:
                print('error')
            current = current.next
            
        final = pre+mid+end
        
        partitionLinkedList = linkedList()

        for i in final:
            partitionLinkedList.insert(i)
        partitionLinkedList.listPrint() 
        

test = linkedList()

arr = [3,5,8,5,10,2,1]

for i in arr:
    test.insert(i)

test.listPrint()

test.partition(5)
