#2.7 Intersection

class Intersect:
    inter = None

class Node:
    def __init__(self,data):
        self.value = data
        self.next = None

class linkedList(Node):
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = Node(data)
        if node.value == 5:
            Intersect.inter = node
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    def intersect(self):
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Intersect.inter

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
        print('\n')

test1 = [1,2,3,4,5,6,7,8,9,10]
test2 = [11,13,19]

list1 = linkedList()
list2 = linkedList()

for i in test1:
    list1.insert(i)
for i in test2:
    list2.insert(i)

list2.intersect()

def intersection(l1,l2):
    pointer1 = list1.head

    while pointer1 != None:
        pointer2 = list2.head
        while pointer2 != None:
            print(pointer1.value,pointer2.value)
            if pointer1 == pointer2:
                return pointer1
            else:
                pointer2 = pointer2.next
        pointer1 = pointer1.next

    return False

result = intersection(list1,list2)
print(result)

    






    
