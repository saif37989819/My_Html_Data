import re

# Step 1: Read article.txt
with open('article.txt', 'r') as file:
    read = file.read()

# Step 2: Find capitalized words
bad = re.findall(r'\b[A-Z][A-Za-z]*\b', read)

# Step 3: Count frequencies
dic = {}

for word in bad:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

# Step 4: Write results to don.txt
with open('don.txt', 'w') as jon:
    for word in dic:
        jon.write(word + ": " + str(dic[word]) + "\n")
