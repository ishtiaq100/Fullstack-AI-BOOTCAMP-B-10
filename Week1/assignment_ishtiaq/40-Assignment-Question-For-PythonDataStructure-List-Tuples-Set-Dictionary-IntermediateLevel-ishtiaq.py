# 1.	Create a list comprehension that returns the squares of only the even numbers from 0–20.
#Tip: Use an if condition inside the comprehension.
# Squares of even numbers from 0 to 20
squares = [x**2 for x in range(21) if x % 2 == 0]

print(squares)


# 2.	Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original.
# Tip: Use sorted() instead of .sort().

nums = [3, 1, 4, 1, 5, 9]

# Create a sorted copy
sorted_nums = sorted(nums)

print("Original List:", nums)
print("Sorted List:", sorted_nums)

# nums = [1, 2, 2, 3, 1, 4, 3]

unique_nums = []

# Remove duplicates while keeping order
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)

# 4.	Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension.
# Tip: Use a nested loop inside the comprehension.
nested_list = [[1, 2], [3, 4], [5]]

# Flatten nested list
flat_list = [num for sublist in nested_list for num in sublist]

print(flat_list)

#5 
names = ['alice', 'Bob', 'charlie', 'DAVID']

# Sort names ignoring case
sorted_names = sorted(names, key=str.lower)

print(sorted_names)

# nums = [10, 20, 30, 40, 50, 60]

# Replace items from index 2 to 4
nums[2:5] = [100, 200]

print(nums)

#7
nums = [7, 2, 7, 4, 7, 5]
value = 7

# Find all indices of the value
indices = [index for index, num in enumerate(nums) if num == value]

print(indices)

# 8.	Create a new list containing only elements that appear exactly once in the original list.
# Tip: Use list.count() inside a comprehension.
nums = [1, 2, 2, 3, 4, 4, 5]

# Keep only elements that appear exactly once
unique_once = [num for num in nums if nums.count(num) == 1]

print(unique_once)

lst = [1, 2, 3, 4]

# Rotate list right by one position
rotated = lst[-1:] + lst[:-1]

print(rotated)


# 10.	Split a list into two lists: one with even numbers, one with odd numbers.
# Tip: Create two comprehensions.

nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Even numbers
even_nums = [num for num in nums if num % 2 == 0]

# Odd numbers
odd_nums = [num for num in nums if num % 2 != 0]

print("Even Numbers:", even_nums)
print("Odd Numbers:", odd_nums)



#tupples mcq
numbers = [1, 2, 3, 4]

# Convert list to tuple
my_tuple = tuple(numbers)

# Unpack tuple into variables
a, b, c, d = my_tuple

print(my_tuple)
print(a, b, c, d)

# 2.	Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements.
# Tip: Use a comprehension: x[1].
t = (('a', 1), ('b', 2), ('c', 3))

# Get all second elements
second_elements = [x[1] for x in t]

print(second_elements)

# 3.	Write a function that returns multiple values (sum, min, max) using a tuple.
# Tip: Return (..., ..., ...) and unpack later.
# Function returning multiple values
def calculate(nums):
    return (sum(nums), min(nums), max(nums))

numbers = [10, 20, 30, 40]

# Unpack returned tuple
total, minimum, maximum = calculate(numbers)

print("Sum:", total)
print("Min:", minimum)
print("Max:", maximum)

# 4.	Combine two tuples (1, 2, 3) and (4, 5) then convert the result to a list.
# Tip: Use + to join them.
t1 = (1, 2, 3)
t2 = (4, 5)

# Combine tuples
combined_tuple = t1 + t2

# Convert tuple to list
result = list(combined_tuple)

print(result)

# t = (1, 2, 2, 3, 4, 2, 3, 3, 3)

most_frequent = None
highest_count = 0

# Check frequency of each unique element
for item in set(t):
    count = t.count(item)

    if count > highest_count:
        highest_count = count
        most_frequent = item

print("Most Frequent Element:", most_frequent)
print("Frequency:", highest_count)

# t1 = (3, 1, 2)
t2 = (2, 3, 1)

# Check if tuples contain same elements
print(sorted(t1) == sorted(t2))

# t = (10, 20, 30, 40, 50, 60)

# Extract last three items
last_three = t[-3:]

print(last_three)

# 8.	Concatenate a tuple with itself three times (repeat operation).
# Tip: Use tuple * 3.
t = (1, 2, 3)

# Repeat tuple three times
result = t * 3

print(result)

nested_tuple = ((1, 2), (3, 4))

# Flatten nested tuple
flat_tuple = tuple(num for subtuple in nested_tuple for num in subtuple)

print(flat_tuple)


# 10.	Store coordinates in tuples and calculate the Manhattan distance.
# Tip: Use absolute difference formula: abs(x1-x2) + abs(y1-y2).

# Store coordinates in tuples
point1 = (2, 3)
point2 = (5, 7)

# Calculate Manhattan distance
distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

print("Manhattan Distance:", distance)


#sets
# 1.	Given two sets, find elements that are in the first set but not the second.
# Tip: Use the - operator.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}

# Elements in set1 but not in set2
result = set1 - set2

print(result)

# 2.	Find common items between three sets using intersection.
# Tip: Use set1 & set2 & set3.
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
set3 = {0, 2, 3, 6}

# Common elements in all three sets
result = set1 & set2 & set3

print(result)

# 3.	Given a sentence, return all unique words in lowercase.
# Tip: Split the string → lowercase → convert to set.
sentence = "Python is great and python is easy"

# Convert to lowercase, split into words, and get unique words
unique_words = set(sentence.lower().split())

print(unique_words)

# 4.	Convert a list with duplicates into a set, then back to a sorted list.
# Tip: Use sorted(set(list)).
nums = [5, 1, 2, 2, 3, 5, 4]

# Remove duplicates using set, then sort
result = sorted(set(nums))

print(result)

# 5.	Check if one set is a strict subset of another.
# Tip: Use < operator.
set1 = {1, 2}
set2 = {1, 2, 3, 4}

# Check strict subset
print(set1 < set2)


# 6.	Use a set comprehension to collect all squares of numbers from 1–15 that are divisible by 3.
# Tip: Write {x*x for x in ... if x % 3 == 0}.
# Set comprehension: squares of numbers 1–15 divisible by 3
result = {x*x for x in range(1, 16) if x % 3 == 0}

print(result)

# 7.	Count how many duplicate values exist in a list using sets.
# Tip: Compare lengths: len(list) - len(set(list)).
nums = [1, 2, 2, 3, 4, 4, 4, 5]

# Count duplicates using set
duplicate_count = len(nums) - len(set(nums))

print(duplicate_count)


#Write a program to remove all vowels from a string using a set. 
#Tip: Use a vowel set and filter characters.

text = "Hello World"

vowels = {'a', 'e', 'i', 'o', 'u'}

# Remove vowels using set filtering
result = ''.join(ch for ch in text if ch.lower() not in vowels)

print(result)

# 9.	Find the symmetric difference between two sets.
# Tip: Use the ^ operator.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Symmetric difference
result = set1 ^ set2

print(result)

# 10.	Check if two strings are anagrams using set comparison (unique characters only).
# Tip: Compare set(str1) with set(str2).
s1 = "listen"
s2 = "silent"

# Check anagram using sets (unique characters only)
print(set(s1) == set(s2))

#Part D — Python Dictionaries (10 Intermediate-Level Questions)

sentence = "apple banana apple orange banana apple"

d = {}

for word in sentence.split():
    d[word] = d.get(word, 0) + 1

print(d)


d = {'a': 1, 'b': 2, 'c': 3}

inverted = {}

for k, v in d.items():
    inverted[v] = k

print(inverted)

d1 = {'a': 1, 'b': 2}
d2 = {'b': 10, 'c': 3}

merged = {**d1, **d2}

print(merged)

words = ["apple", "ant", "banana", "ball", "cat"]

grouped = {}

for w in words:
    grouped.setdefault(w[0], []).append(w)

print(grouped)

d = {'a': 40, 'b': 60, 'c': 80, 'd': 30}

filtered = {k: v for k, v in d.items() if v > 50}

print(filtered)

data = {
    "user": {
        "profile": {
            "name": "Ali"
        }
    }
}

name = data.get("user", {}).get("profile", {}).get("name", "Not Found")

print(name)

cubes = {x: x**3 for x in range(1, 11)}

print(cubes)

d = {'a': 10, 'b': 50, 'c': 30}

max_key = max(d, key=d.get)

print(max_key)

keys = ['a', 'b', 'c']
values = [1, 2, 3]

d = dict(zip(keys, values))

print(d)

d = {'a': 1, 'b': None, 'c': 3, 'd': None}

cleaned = {k: v for k, v in d.items() if v is not None}

print(cleaned)
