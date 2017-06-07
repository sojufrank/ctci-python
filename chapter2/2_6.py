#2.6 Palindrome

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

    def palindrome(self):
        current = self.head
        str = ''
        while current != None:
            str += current.value
            current = current.next

        if str == str[::-1]:
            return True
        else:
            return False

            


test = linkedList()
string = 'eye'
for c in string:
    test.insert(c)
test.listPrint()
result = test.palindrome()
print(result)

