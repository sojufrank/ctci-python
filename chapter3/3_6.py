#3.6 Animal Shelter

class Node:
    def __init__(self,d,o):
        self.value = d
        self.order = o
        self.next = None
        self.prev = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,data, count):
        node = Node(data, count)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def peek(self):
        return self.tail.value

    def getOrder(self):
        return self.tail.order

    def pop(self):
        r = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return r      

    def listPrint(self):
        current = self.head
        while current != None:
            print(current.value,current.order)
            current = current.next
        print('\n')

class animal:
    def __init__(self):
        self.count = 0
        self.dogs = linkedList()
        self.cats = linkedList()

    def enqueue(self,data):
        if data == 'dog':
            self.dogs.push(data, self.count)
            self.count += 1
        else:
            self.cats.push(data, self.count)
            self.count += 1
            
    def dequeueAny(self):
        if self.cats.getOrder() < self.dogs.getOrder():
            return self.cats.pop()
        else:
            return self.dogs.pop()
        

    def dequeueDog(self):
        self.dogs.pop()
        
    def dequeueCat(self):
        self.cats.pop()

    def printDogs(self):
        self.dogs.listPrint()

    def printCats(self):
        self.cats.listPrint()

    def printAll(self):
        d = self.dogs.tail
        c = self.cats.tail
        while c or d:
            if c != None:
                if d == None:
                    print(c.value,c.order)
                    c = c.prev
                else:  
                    if c.order < d.order:
                        print(c.value,c.order)
                        c = c.prev
            if d != None:
                if c == None:
                    print(d.value,d.order)
                    d = d.prev
                else:
                    if d.order < c.order:
                        print(d.value,d.order)
                        d = d.prev
        print('\n')
            

test = animal()
arr = ['dog','cat','cat','dog','dog','dog','cat','dog','cat','cat','cat']

for s in arr:
    test.enqueue(s)

test.printAll()

test.dequeueAny()
test.dequeueAny()
test.printAll()
        

    



    


