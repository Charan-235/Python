s = "hello world"
freq_dict = {}
for char in s:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
result = ""
for char in s:
    freq = freq_dict[char]
    if char.isalpha():
        shift = 65 if char.isupper() else 97
        new_char = chr((ord(char) - shift + freq) % 26 + shift)
        result += new_char
    else:
        result += char
print("Original string:", s)
print("Modified string:", result)
