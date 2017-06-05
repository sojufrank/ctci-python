#1.8 Zero Matrix

#matrix = [[1,0],[1,1]]
#matrix = [[0,1,1],[1,1,1],[1,1,1]]
matrix = [[1,1,0,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

def p(m):
    for arr in m:
        print(arr)
p(matrix)

def zero(m):

    row = len(m)
    col = len(m[0])
    d = {} #create dict to keep track of changes in the matrix

    #build dict
    for i in range(row):
        for j in range(col):
            k = str(i)+str(j)
            d[k] = False

    for i in range(row):
        for j in range(col):
            k = str(i)+str(j)
            if m[i][j] == 0 and d[k] == False:
                d[k] = True
                for l in range(row):
                    m[i][l] = 0
                    k = str(i)+str(l)
                    d[k] = True
                    for o in range(col):
                        m[o][j] = 0
                        k = str(o)+str(j)
                        d[k] = True

    return m

result = zero(matrix)
print('\n')
p(result)


