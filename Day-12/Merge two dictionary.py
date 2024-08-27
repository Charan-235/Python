def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 2, 'e': 30, 'f': 40}
merged_dict = merge_dicts(dict1, dict2)
print("Merged Dictionary:", merged_dict)  #Output:Merged Dictionary: {'a': 2, 'b': 2, 'c': 3, 'e': 30, 'f': 40}
