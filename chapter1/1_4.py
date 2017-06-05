# 1.4 Palindrome Permutation:
# i spend a lot of time trying to implement an algorithm for permutations but that is not needed
# a better way to look at this is
# check if each character has an even amout of characters
# 1 odd character is allowed.  in the middle

string ='Tact Coa'

def palindrome(s):
    s = s.lower().replace(' ', '')
    d = dict.fromkeys(s,False)
    counter = 0
    
    for c in s:
        if d[c] == False:
            d[c] = True
        else:
            d[c] = False

    for k in d:
        if d[k] == True:
            counter += 1

    if counter > 1:
        return False
    else:
        return True
    

result = palindrome(string)
print(result)
