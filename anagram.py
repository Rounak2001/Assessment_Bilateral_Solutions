
def isAnagram(str1,str2):
    count = [0] * 26
       
    for x in str1:
        count[ord(x) - ord('a')] += 1
        
    for x in str2:
        count[ord(x) - ord('a')] -= 1
        
    for val in count:
        if val != 0:
            return False
        
    return True

str1 = input("Enter the first string:\n")
str2 = input("Enter the second string:\n")
result = isAnagram(str1,str2)
print(result)