def min_jumps(arr):
    n = len(arr)
    jumps = [float('inf')] * n
    jumps[0] = 0
    for i in range(1, n):
        for j in range(i):
            if j + arr[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)

    return jumps[-1]
arr = [1,3,5,8,9,1,6,7,6,8,9]
print(min_jumps(arr))  

