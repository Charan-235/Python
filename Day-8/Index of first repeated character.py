s = 'banana'
sorted_s = " ".join(sorted(s))
index = -1
for i in range(1,len(sorted_s)):
    if sorted_s[i] == sorted_s[i-1]:
        index =i
        break
print("sorted string:",sorted_s)
print("index of first repeated character is :",index)
