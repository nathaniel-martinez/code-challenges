"""
Given two strings, return True if the first string is a substring of the second Stirng. If it is not return False
Make sure that your function is case insensitive and does not relly on previous funcitons.
"""

def is_substr(s1, s2):
    str1 = s1.lower()
    str2 = s2.lower()
    i = 0
    str1Len = len(str1)
    for c2 in str2:
        if str1[i] == c2:
            i = i + 1
        elif str1[0] == c2:
            i = 1
        else:
            i = 0
        if i == str1Len:
            return True
    return False

print(is_substr("abc", "abcde")) # True
print(is_substr("aBc", "AAAabcde")) # True
print(is_substr("abasde", "s")) # False
print(is_substr("abcds", "asadfwwersdfbcds"))# False
