def longest_common_subsequence(s1, s2):
    a = [i for i in s1 if i in s2]
    return "".join(a)
s1 = "abc"
s2 = "acd"
print(longest_common_subsequence(s1, s2)) 
