# 1.3 URLify
# not sure if i am supposed to strip the whitespace at end of string, but i did

string = 'Mr John Smith '

def urlify(s):
    s = s.rstrip()
    s = s.replace(' ', '%20')
    return s

result = urlify(string)
print(result)
