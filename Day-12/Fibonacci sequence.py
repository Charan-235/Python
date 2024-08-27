#Create a generator function that generates the fibonacci sequence number of elements
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fibonacci(5)))   #OutPut:[0, 1, 1, 2, 3]
