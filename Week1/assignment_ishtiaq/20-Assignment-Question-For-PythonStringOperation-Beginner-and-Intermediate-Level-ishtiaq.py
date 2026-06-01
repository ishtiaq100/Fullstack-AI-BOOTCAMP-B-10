#1
stringTxt = 'hello world'
print(len(stringTxt))

#2 lower upper
print(stringTxt.lower())
print(stringTxt.upper())

print(stringTxt[0],stringTxt[-1])

print(stringTxt.count('l'))

text = " data science"
search="science"
result = search in text
print(result)

#6 slice the string
sliceString = "programming"
print(sliceString[3:8])

#7 reverse the string
txtData = "python"
print(txtData[::-1])

#8Replace substring
txtReplace = "I love apples. Apples are great!"
print(txtReplace.replace("apples","orange"))
#9 split 
txtSplit = "split this sentence"
getSplitTxt = txtSplit.split()
print("-".join(getSplitTxt))

removePad = " hello pakistan"
print(removePad.strip())

#Intermediate level
#1
inputTxt = "Hello, World! 123"
vowels = 0
constant=0
for txt in inputTxt:
                    if txt.isalpha():
                                        vowelstxt = 'aeiou'
                                        if txt.lower() in vowelstxt:
                                            vowels +=1
                                        else:
                                            constant +=1
print("Total vowels",vowels)

print("Total constant",constant)



#2
s = "A man, a plan, a canal: Panama!"

# Remove non-alphanumeric characters and convert to lowercase
normalized = ''.join(ch.lower() for ch in s if ch.isalnum())

# Check palindrome
is_palindrome = normalized == normalized[::-1]

print(is_palindrome)


#3 title case
sentence = "hELLOwORLD from PYTHON"
words = sentence.split()
print(words)
result=[]
for word in words:
        if word:
                formated_word = word[0].upper()+word[1:].lower()
        result.append(formated_word)
print(" ".join(result))    

#4
s="aaaa"
sub="aa"
indices=[]
for i in range(len(s)-len(sub)+1):
        if s[i:i + len(sub)]== sub:
                indices.append(i)

print(indices)

s = "Baa Baa Black Sheep"

freq = {}

# Convert to lowercase and iterate
for ch in s.lower():
    
    # Skip spaces
    if ch != ' ':
        
        # Count frequency
        freq[ch] = freq.get(ch, 0) + 1

print(freq)



s1 = "Listen"
s2 = "Silent"

# Normalize strings:
# keep only letters and convert to lowercase
str1 = ''.join(ch.lower() for ch in s1 if ch.isalpha())
str2 = ''.join(ch.lower() for ch in s2 if ch.isalpha())

# Check anagram
is_anagram = sorted(str1) == sorted(str2)

print(is_anagram)

#7
s = "aaabbcaaaa"

compressed = ""
count = 1

# Loop through string
for i in range(len(s) - 1):

    # If same character, increase count
    if s[i] == s[i + 1]:
        count += 1

    # If character changes
    else:
        compressed += s[i] + str(count)
        count = 1

# Add last character group
compressed += s[-1] + str(count)

print(compressed)


sentence = "Find the longest_word here!"

longest_word = ""

# Split sentence into tokens
tokens = sentence.split()

for token in tokens:
    
    # Keep only alphabetic characters
    clean_word = ''.join(ch for ch in token if ch.isalpha())
    
    # Check length
    if len(clean_word) > len(longest_word):
        longest_word = clean_word

print(longest_word)


s = "banana"

seen = set()
result = ""

# Loop through each character
for ch in s:
    
    # Add only if not already seen
    if ch not in seen:
        seen.add(ch)
        result += ch

print(result)




email = "john.doe@example.com"

# Split username and domain
username, domain = email.split('@')

# Mask username
if len(username) >= 2:
    masked_username = (
        username[0] +               # first character
        '*' * (len(username) - 2) + # middle stars
        username[-1]                # last character
    )
else:
    masked_username = username

# Combine again
masked_email = masked_username + '@' + domain

print(masked_email)