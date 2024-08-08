import math
num=int(input("Enter the value:"))
digits=str(num)
sum=0
for i in digits:
    sum+=math.factorial(int(i))
if sum==num:
    print(f"{num} is a strong number")
else:
   print(f"{num} is not a strong number") 
