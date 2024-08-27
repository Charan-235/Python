dict_list = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]

# Sort by 'age' key in ascending order
sorted_dict_list = sorted(dict_list, key=lambda x: x['age'])
print(sorted_dict_list)     #Output:[{'name': 'Bob', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}]

# Sort by 'name' key in alphabetical order
sorted_dict_list = sorted(dict_list, key=lambda x: x['name'])
print(sorted_dict_list)     #Output:[{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}, {'name': 'John', 'age': 25}]
