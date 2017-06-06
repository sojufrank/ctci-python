#1.9 String Rotation:
#i did not do this question correctly.  will return later

string1 = 'waterbottle'
string2 = 'erbottlewat'

def rotation(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        for j in range(len(s1)):
            if s1[i] == s2[j]:
                x = s2[:j]
                y = s2[j:]
                if y+x == s1:
                    return True
    return False
                

def issubstring(s1,s2):
    
    pass

result = rotation(string1,string2)
print(result)
