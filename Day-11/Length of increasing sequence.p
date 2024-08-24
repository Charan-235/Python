def longest_increasing_sequence(seq):
    if not seq:
        return 0
    length = 1
    max_length = 1
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            length += 1
        else:
            max_length = max(max_length, length)
            length = 1
    return max(max_length, length)
a = (10, 22, 9, 33, 41, 50, 41, 60)
print("Length of longest increasing sequence:", longest_increasing_sequence(a))
