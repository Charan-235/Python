number = 9875
while number >= 10:
    digits = [int(digit) for digit in str(number)]
    number = sum(digits)
print(f"The single digit sum is: {number}")
