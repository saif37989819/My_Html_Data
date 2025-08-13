import re

text = "My age is 25 and my brother is 30."

# Yeh pattern pehla number dhoondhta hai
result = re.search(r'\d+', text)

# Agar match mila ho to usay print karo
if result:
    print(result)  # Output: 25
# re.search(): Pehla match return karta hai (poori string mein se)
# \d+ : 1 ya zyada digits ka pattern
# result.group(): milne wala match string ki form mein


# re.findall(): jitne bhi matches hain un sab ki list return karta hai
# \d+ : 1 ya zyada digits
import re

text = "Ali has 2 pens and 3 books."

# Yeh pattern text mein jitne bhi digits hain un sab ko dhoondhta hai
numbers = re.findall(r'\d+', text)

print(numbers)  # Output: ['2', '3']


# re.match(): sirf string ke start mein match dhoondhta hai
# 'Hello' agar pehle hi likha ho, tabhi match karega
import re

text = "Hello, how are you?"

# Yeh sirf start se match karta hai
match = re.match(r'Hello', text)

if match:
    print(match.group())  # Output: Hello


# re.sub(): given pattern ko replace karta hai
# \d : har digit ko
# 'X' : naya character jisse replace karna hai
import re

text = "Call me at 123-456-7890."

# Yeh pattern har digit ko 'X' se replace karega
new_text = re.sub(r'\d', 'A', text)

print(new_text)  # Output: Call me at XXX-XXX-XXXX.

# re.split(): pattern ke mutabiq string ko todta hai (split karta hai)
# [;, ]: comma, semicolon, ya space pe todna
import re

text = "apple;banana;grapes, orange"

# Comma, semicolon, ya space se string split karo
fruits = re.split(r'[ ;]', text)

print(fruits)  # Output: ['apple', 'banana', 'grapes', 'orange']

# re.compile(): regex pattern ko ek object mein convert karta hai
# baar baar use karne ke liye efficient hota hai
import re

text = "He is 21 and she is 25."

# Pattern ko compile kar ke baar baar use karne ke liye tayar kiya
pattern = re.compile(r'\d+')

# ab findall, search ya match isi pattern pe apply ho sakta hai
numbers = pattern.findall(text)

print(numbers)  # Output: ['21', '25']




