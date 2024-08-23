array = list(map(int, input("Enter the array elements (space separated): ").split()))
repeated_elements = [element for element in set(array) if array.count(element) > 1]
print("Repeated elements: ", repeated_elements)
