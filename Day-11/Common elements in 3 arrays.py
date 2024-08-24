def common(a1,a2,a3):
    return list(set(a1) & set(a2) & set(a3))
    
a1 = [1,2,3,4,5]
a2 = [2,3,7,8,9]
a3 = [10,23,2,3,11]
c = common(a1,a2,a3)
print("common elements: ",c)
