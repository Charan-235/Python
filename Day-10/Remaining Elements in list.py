n = [1, 3, 5, 7, 8]
m = ['a', 'b', 'c', 'd', 'u', 'h', 'i']
l = min(len(n), len(m))
mer= [val for pair in zip(n[:l], m[:l]) for val in pair]
rem= n[l:] + m[l:]
print("Merged List:", mer)
print("Remaining List:", rem)
