sen = input("enter a sentense : ")
width = int(input("enter width : "))
words = sen.split()
lines = []
line = " "
for word in words:
    if len(line)+len(word)+1>width:
        lines.append(line.ljust(width))
        line = word
    else:
        line+=" "+word
lines.append(line.ljust(width))
print("\n".join(lines))
            
