#2.2 Return Kth to Last
# learned a few new things about recursion and recursion returns from this challenge

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

    def findLastElem(self,n):
        current = self.head
        flag = False

        def rec(pointer, n, f):
            elem = 0
            while pointer != None:
                if pointer.next == None:
                    if n == 1:
                        elem = pointer.value
                        f = True
                        return elem, f
                    return 1, f
                else:
                    x, f = rec(pointer.next, n, f)
                    if f == True:
                        return x, f
                    else:
                        x += 1
                        if x == n:
                            elem = pointer.value
                            f = True
                            return elem, f
                    return x, f
            return elem

        return rec(current, n, flag)

ll = linkedList()
test = 'hello world'

for i in test:
    ll.insert(i)

#ll.listPrint()
result = ll.findLastElem(1)

print(result)
