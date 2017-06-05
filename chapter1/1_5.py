#ctci 1.5 One Away

str1 = 'tales'
str2 = 'pales'

def one(s1,s2):

    #if string lengths are the same check replace
    if len(s1) == len(s2):
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
        if counter == 1:
            return True
        else:
            return False
    #if length of s1 is greater than s2 check remove
    elif len(s1) > len(s2):
        diff = len(s1) - len(s2) # get the diff in lengths
        s2 += '*'* diff #add placeholder '*' diff times
        count = 0
        for i in range(len(s1)):
            #if char is equal or char is '*' skip
            if (s2[i] == '*' and i == len(s2)) or s1[i] == s2[i]:
                pass
            #if chars are different rebuild s2 to keep comparing
            else:
                s2 = s2[:i]+s1[i]+s2[i+1:]
                count += 1
        #if number of changes is not 1 then return False
        if count == 1:
            return True
        else:
            return False
    #if length of s1 is lesser than s2 check insert
    elif len(s1) < len(s2):
        diff = len(s2) - len(s1)
        s1 += '*'*diff
        count = 0
        for i in range(len(s2)):
            if (s1[i] == '*' and i == len(s1)) or s2[i] == s1[i]:
                pass
            else:
                s1 = s1[:i]+s2[i]+s1[i:]
                count += 1
        if count == 1:
            return True
        else:
            return False
    return 'error'

res = one(str1,str2)
print(res)
