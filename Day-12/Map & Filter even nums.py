#Python program that uses map and filter functions to first square all elements in list and then filter out all  sqaures that are even numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)    #Output: Squared numbers:[1,4,9,16,25]
odd_squares = list(filter(lambda x: x % 2 != 0, squared_numbers))
print("Odd squares:", odd_squares)            #Output: Odd squares: [1,9,25]
