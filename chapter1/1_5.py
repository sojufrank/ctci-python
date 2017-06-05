#ctci 1.5

str1 = 'pales'
str2 = 'pal'

def one(s1,s2):

    #bool = {'replace':False, 'insert':False, 'remove':False}
    
    if len(s1) == len(s2): #replace
        #bool['replace'] = True
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False
    elif len(s1) > len(s2): #remove
        #bool['remove'] = True
        minus = len(s1) - len(s2)
        s2 += '*'* minus
        s = ''
        count = 0
        for i in range(len(s1)):
            if (s2[i] == '*' and i == len(s2)) or s1[i] == s2[i]:
                pass
            else:
                print(s2)
                s2 = s2[:i]+s1[i]+s2[i+1:]
                print(s2)
                count += 1
        if count == 1:
            return True
        else:
            return False
    

            
        
        
    #elif len(s1) < len(s2):
        #bool['insert'] = True
        

    
        

res = one(str1,str2)
print(res)
