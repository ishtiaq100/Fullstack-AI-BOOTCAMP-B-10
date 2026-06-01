# 1.	Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements.
# Tip: Use nums[0] and nums[-1].
nums = [3, 1, 4, 1, 5]
print(nums[0],nums[-1])



# 2.	Find the length of the list colors = ['red', 'blue', 'green'].
# Tip: Use len(colors).
colors = ['red', 'blue', 'green']
print(len(colors))


# 3.	Append 'yellow' to the list colors = ['red', 'blue'].
colors = ['red', 'blue']
colors.append('yellow')
print(colors)

# Tip: Use append().
# 4.	Insert 'orange' at index 1 in fruits = ['apple', 'banana'].
fruits = ['apple', 'banana']
fruits.insert(2,'orange')
print(fruits)
# Tip: Use insert(index, value).
# 5.	Remove 'banana' from fruits = ['apple', 'banana', 'grapes'].
# Tip: Use remove(value).
fruits.remove('banana')
print(fruits)


# 6.	Pop the last element from items = [10, 20, 30] and print the popped value.
# Tip: Call items.pop().
items = [10, 20, 30]
items.pop()
print(items)
# 7.	Check if 3 is in the list nums = [1, 2, 3, 4].
# Tip: Use the in operator.
nums = [1, 2, 3, 4]
result =3 in nums
print(result)
# 8.	Print the slice [2, 3] from the list [0, 1, 2, 3, 4].
# Tip: Use slicing: a[2:4].
listData = [0, 1, 2, 3, 4]
print(listData[2:4])

# 9.	Replace the element at index 1 in a = [5, 10, 15] with 12.
# Tip: Use assignment: a[1] = 12.
a = [5, 10, 15]
a[1]=12
print(a)

# 10.	Count how many times 2 appears in [1, 2, 2, 3, 2].
# Tip: Use list.count(value).
listmdata =[1, 2, 2, 3, 2]
counter = listmdata.count(2)
print(counter)






# 1.	Create a tuple t = (10, 20, 30) and print the second element.
# Tip: Tuples use indexing: t[1].
t = (10, 20, 30)
print(t[2])


# 2.	Find the length of tuple ('a', 'b', 'c').
# Tip: Use len().
newtpl = ('a', 'b', 'c')
print(len(newtpl))
# 3.	Unpack the tuple (4, 5) into variables x and y.
# Tip: x, y = (4, 5).
x, y = (4, 5)
print(x,y)
# 4.	Check if 'b' is in the tuple ('a', 'b', 'c').
# Tip: Use 'b' in tuple.
my_tuple = ('a', 'b', 'c')

# Check if 'b' exists in tuple
print('b' in my_tuple)

# 5.	Create an empty tuple and print its type.
# Tip: Empty tuple is ().
etupil = ()
print(type(etupil))


# 6.	Concatenate (1, 2) and (3, 4) into a new tuple.
# Tip: Use + operator.
etupil = ((1,2)+(3,4))
print(etupil)
# 7.	Repeat (7,) three times.
# Tip: Use tuple * number.
etupil = (7,)*3
print(etupil)
# 8.	Find the index of 2 in (1, 2, 3, 2).
# Tip: Use index() method.
findex = (1, 2, 3, 2)
print(findex.index(2))

# 9.	Count how many times 2 appears in (1, 2, 3, 2).
# Tip: Use count() method.
numtupl = (1, 2, 3, 2)
print(numtupl.count(2))


# 10.	Create a single‑element tuple containing the value 5.
# Tip: Remember to use a comma: (5,).
newtulp = (5,)
print(newtulp)





# 1.	Create a set from [1, 2, 2, 3] and print it.
# Tip: Use set(list).
# Create set directly using curly braces
my_set = {1, 2, 2, 3}

print(my_set)
# 2.	Add element 4 to the set {1, 2, 3}.
# Tip: Use add().
myset = {1, 2, 3}
myset.add(4)
print(myset)

# 3.	Remove element 2 from the set {1, 2, 3}.
# Tip: Use remove().
myset = {1, 2, 3}
myset.remove(2)
print(myset)




# 4.	Check if 5 is in the set {1, 3, 5}.
# Tip: Use in operator.
newset = {1,3,5}
resultdmt = 5 in newset
print(resultdmt)
# 5.	Find the length of set {10, 20, 30}.
# Tip: Use len().
nset ={10, 20, 30}

print(len(nset))


# 6.	Clear all elements from the set {1, 2, 3}.
# Tip: Use clear().
tm ={1, 2, 3}
print(tm.clear())

# 7.	Create a set {'a', 'b'} and add 'c' only if it’s missing.
adset={'a','b'}
adset.add('c')
print(adset)

# Tip: Check membership first: if 'c' not in s:.


# 8.	Convert list ['a', 'a', 'b'] into a set to remove duplicates.
# Tip: Casting removes duplicates automatically.

letters = ['a', 'a', 'b']

# Convert list to set
unique_letters = set(letters)

print(unique_letters)

# 9.	Create two sets and print their union.
# Tip: Use set1 | set2.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union of two sets
print(set1 | set2)


# 10.	Create two sets and print their intersection.
# Tip: Use set1 & set2.
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Intersection of two sets
print(set1 & set2)




# 1.	Create a dictionary {'name': 'Ali', 'age': 25} and print the name.
# Tip: Use d['name'].
d = {'name': 'Ali', 'age': 25}

# Print name
print(d['name'])
# 2.	Add key 'city': 'Lahore' to a dictionary.
# Tip: Use assignment: d['city'] = 'Lahore'.
d = {'name': 'Ali', 'age': 25}

# Add new key-value pair
d['city'] = 'Lahore'

print(d)
# 3.	Change 'age' in {'name': 'Ali', 'age': 25} to 30.
# Tip: Assign a new value: d['age'] = 30.
d = {'name': 'Ali', 'age': 25}

# Update age
d['age'] = 30

print(d)
# 4.	Delete key 'age' from a dictionary.
# Tip: Use del d['age'].
d = {'name': 'Ali', 'age': 25}

# Delete the key 'age'
del d['age']

print(d)
# 5.	Check if key 'salary' exists in a dictionary.
# Tip: Use in operator.
d = {'name': 'Ali', 'age': 25}

# Check if key exists
print('salary' in d)
# 6.	Print all keys from {'a': 1, 'b': 2}.
# Tip: Use d.keys().
d = {'a': 1, 'b': 2}

# Get all keys
print(d.keys())
# 7.	Print all values from a dictionary.
# Tip: Use d.values().
d.values()
# 8.	Iterate and print key‑value pairs from {'x': 10, 'y': 20}.
# Tip: Use for k, v in d.items().
d = {'x': 10, 'y': 20}

# Iterate through key-value pairs
for k, v in d.items():
    print(k, v)
# 9.	Use get() to safely read key 'score' from an empty dictionary.
# Tip: Use d.get('score', default_value).
d = {}

# Safely get value for 'score'
print(d.get('score', 0))
# 10.	Create a dictionary from two lists: keys = ['a','b'], values = [1,2].
# Tip: Use dict(zip(keys, values)).
keys = ['a', 'b']
values = [1, 2]

# Create dictionary from two lists
d = dict(zip(keys, values))

print(d)