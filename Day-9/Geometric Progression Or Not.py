s = [2,6,18,54,162]
if len(s)<2:
    print("seq must have 2 num")
else:
    r = s[1]/s[0]
    for i in range (2,len(s)):
        if s[i]/s[i-1]!=r:
            print("not gp")
            break
        else:
            print("gp")
        
