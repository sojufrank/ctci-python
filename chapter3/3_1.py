#3.1 Three in One

arr1 = range(0,75)
arr2 = range(100,125)
arr3 = range(210,250)

length = 0
if len(arr1) > length:
    length = len(arr1)
if len(arr2) > length:
    length = len(arr2)
if len(arr3) > length:
    length = len(arr3)

stack = [None]*(length*3)

pointer = [0,length,length*2]

def pop(array, stackN):
    array[pointer[stackN]] = None
    pointer[stackN] -= 1
    
def push(array, stackN, data):
    array[pointer[stackN]] = data
    pointer[stackN] += 1

for i in range(len(arr1)):
    push(stack, 0, i)
for i in range(len(arr2)):
    push(stack, 1, i)
for i in range(len(arr3)):
    push(stack, 2, i)    

#print(len(stack),pointer,length)
pop(stack, 0)
for i in range(3):
    pop(stack,1)
#print(len(stack),pointer,length)
for i in range(5):
    push(stack,2,i+1000)
#print(stack)
