numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter out even numbers and square the remaining odd numbers
squared_odd_numbers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(squared_odd_numbers) #Output:[1,9,25,49,81]
