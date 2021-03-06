#1.7 Rotate Matrix
# quite hard to break down.  will return and review again

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

#matrix = [[1,2],[3,4]]
#matrix = [[1,2,3],[4,5,6],[7,8,9]]

for a in matrix:
    print(a)

def rotate(m):

    n = len(matrix)

    for layer in range(int(n/2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            off = i - first
            
            top = m[first][i]
            m[first][i] = m[last - off][first]
            m[last-off][first] = m[last][last - off]
            m[last][last-off] = m[i][last]
            m[i][last] = top

    return m


result = rotate(matrix)


print(' ')

for arr in result:
    print(arr)
