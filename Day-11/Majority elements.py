def majority_element(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, freq in count.items():
        if freq > len(arr) / 2:
            return num
    return None
a = [22, 22, 22,22, 22, 41, 50, 41, 60]
print("Majority element:", majority_element(a))
