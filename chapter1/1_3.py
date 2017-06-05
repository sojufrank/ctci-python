# 1.3 URLify

string = 'Mr John Smith '

def urlify(s):
    s = s.rstrip()
    s = s.replace(' ', '%20')
    return s

result = urlify(string)
print(result)
