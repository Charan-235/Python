def countmatches(str1,str2):
    matches = 0
    for i in range (min(len(str1),len(str2))):
        if str1[i] == str2[i]:
            matches+=1
            return matches
string1 = "apple"
string2 = "aabbc"
print("num of index :",countmatches(string1,string2))
