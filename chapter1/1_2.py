# 1.2 Check Permutation
#take each string and place them into a dictionary
#increment value counter for each character in string

string1 = 'abc'
string2 = 'cba'

def Permutation(s1, s2):

    d1 = dict.fromkeys(s1,0)
    d2 = dict.fromkeys(s2,0)

    for c in s1:
        d1[c] += 1
    for c in s2:
        d2[c] += 1
    if d1 == d2:
        return True
    else:
        return False
        
result = Permutation(string1, string2)
print(result)
