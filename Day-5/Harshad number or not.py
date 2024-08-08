num=int(input("enter a number"))
sod=sum(int(digit) for digit in str(num))
if num % sod == 0:
    print("harshad number")
else:
    print("not harshad number")
    
