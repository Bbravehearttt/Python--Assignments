  # Most frequent number

numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3, 3, 4, 4, 4]
max(numbers)
a = max(numbers,  key = numbers.count)  # The most frequent number
b = numbers.count(max(numbers, key = numbers.count))  # How many times repeat it.
print("The most frequent number is {} and it was {} times repeated".format(a, b))




