# 1.6 String Compression

string = 'aabcccccaaa'

def compression(s):
    compressed = ''
    count = 0

    for i in range(len(s)):
        count += 1

        if i >= len(s)-1 or s[i] != s[i+1]:
            compressed += s[i]+str(count)
            count = 0

    return compressed
    

result = compression(string)
print(result)

