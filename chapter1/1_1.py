#ctci 1.1 Is Unique

string = 'abcde'

def unique(s):

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if i != len(s):
                if s[i] == s[j]:
                    return False
    return True
            
result = unique(string)
print(result)
