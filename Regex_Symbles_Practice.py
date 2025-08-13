import re

text = "Invoice numbers: INV-1023, INV-5678, and INV-999."

digits = re.findall(r'\d+', text)
print(digits)  # Output: ['1023', '5678', '999']

import re

text = "Usernames: Saif_Ullah,  Khan123, Hello_World!"

words = re.findall(r'\w+', text)
print(words)  # Output: ['Usernames', 'Saif_Ullah', 'Khan123', 'Hello_World']

text ="Name:  Ali Khan\nAge:21\nCountry  :Pakistan"

# \s har whitespace character (space, tab, newline) ko match karta hai
spaces = re.findall(r'\s', text)

print(spaces)  # Output: ['\t', ' ', '\n', '\t', '\n', ' ']
# Har jagah jahan space ya tab ya newline hai — usay match karega


text = "Files: Dc1_pdf, ..image2.jpg, ...audio3.mp3"

# dot (.) kisi bhi aik character ko match karta hai
matches = re.findall(r'\.+\.\w+', text)

print(matches)  # Output: ['doc1pdf', 'image2.jpg', 'audio3.mp3']
# \w+\.\w+ ka matlab: word + dot + word (file names ke liye perfect)


text = "He said: ah, aah, aaah!"

# a+h+ ka matlab: kam az kam aik 'a' aur aik 'h' lazmi hone chahiye
sounds = re.findall(r'a+', text)

print(sounds)  # Output: ['ah', 'aah', 'aaah']
# Yeh expression natural emotions jese sounds ko pakarta hai


text = "Color, Colour, Colored"

# u? ka matlab: 'u' ho bhi sakta hai aur nahi bhi
matches = re.findall(r'Colou?r', text)

print(matches)  # Output: ['Color', 'Colour']
# UK aur US spelling difference handle karne ke liye yeh useful hai


text = "Saif: Disk full"

# ^Error ka matlab: string start honi chahiye 'Error' se
if re.match(r'^', text):
    print("Line starts with 'Error'")
# Sirf tab match hoga jab 'Error' sabse pehle likha ho


text = "Pets: cats, Dogs, rats, bats"

# [cdr]ats ka matlab: c ya d ya r se shuru hone wale 'ats' wale words
animals = re.findall(r'[cdr]ats', text)

print(animals)  # Output: ['cats', 'dogs', 'rats']
# Yeh sirf un words ko match karega jo specified letters se shuru hote hain


text = "Prices: $200, $350, $499"

# \$ ko escape kiya gaya hai — aur (\d+) numbers ko group karta hai
prices = re.findall(r'\$(\d+)', text)

print(prices)  # Output: ['200', '350', '499']
# Brackets se hum sirf digits ko extract kar rahe hain, $ nahi

text = "I will drink coffee tea or juice."

# coffee|tea|juice ka matlab: teenon mein se koi bhi match ho sakta hai
drinks = re.findall(r'coffee|tea|juice', text)

print(drinks)  # Output: ['coffee', 'tea', 'juice']
# OR operator multiple possible matches allow karta hai

import re

text = " test@gmail.com, invalid@.com, user_123@yahoo.com"

# \w+ : aik ya zyada word characters
# @ : exact '@' symbol
# \w+ : domain name
# \. : dot (.)
# (com|net|org) : end hona chahiye in teenon me se kisi pe
pattern = r'\b\w+@\w+\.(com|net|org)\b'

emails = re.findall(r'\b\w+@\w+\.(com|net|org)\b', text)
print(emails)
# Sirf valid looking email addresses match karega

text = "Phone: 0300-1234567, +92-300-1234567, 0345.7654321"

# (\+92|03)\d{2} : ya to +92 ya 03 se shuru ho
# [-.] : dash ya dot use ho sakta hai
# \d{7} : 7 digits hone chahiye baad mein
pattern = r'(\+92|03)\d{2}[-.]\d{7}'

phones = re.findall(pattern, text)
print(phones)
# Multiple phone number formats handle karega

text = "Ali went to Lahore. Then Sara met with Dr. Ahmed."

# \b[A-Z][a-z]+ : capital letter se start hone wale words
names = re.findall(r'\b[A-Z][a-z]+', text)
print(names)
# Capital names ko dhoondta hai

text = "Today is 12.08.2025 and tomorrow is 13/08/2025"

# \d{2} : 2 digits
# [-/] : dash ya slash
# \d{4} : 4 digit year
pattern = r'\b\d{2}[./]\d{2}[./]\d{4}\b'

dates = re.findall(pattern, text)
print(dates)
# Date formats ko recognize karta hai

text = "This is is a a test test test."

# \b(\w+)\s+\1 : koi word, space, aur wohi word dobara
repeats = re.findall(r'\b(\w+)\s+\1\b', text)
print(repeats)
# Repeat hone wale words ko pakarta hai

text = "This is is a a test test."

# \b(\w+)\s+\1 : koi word, space, aur wohi word dobara
repeats = re.findall(r'\b(\w+)\s+\1\b', text)
print(repeats)
# Repeat hone wale words ko pakarta hai


text = "Follow @saif and support #PythonRegex"

# @\w+ : mention
# #\w+ : hashtag
mentions = re.findall(r'[@#]\w+', text)
print(mentions)
# Twitter-style mentions aur hashtags


text = "Hello there! Are you okay? Let's go."

# .+?[.!?] : sentence jo kisi punctuation pe khatam ho
sentences = re.findall(r'.+?[.!?]', text)
print(sentences)
# Har proper sentence ko match karega


text = "My passwords: Abc123!, xyz123, @Secure1"

# (?=.*[A-Z]) : kam az kam aik capital letter
# (?=.*[a-z]) : kam az kam aik small letter
# (?=.*\d) : aik digit
# (?=.*[@$!%*?&]) : special char
# .{6,} : total 6 ya zyada chars
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{6,}'

strong_passwords = re.findall(pattern, text)
print(strong_passwords)
# Sirf strong passwords ko nikaalta hai

text = "Meeting at 08:30 AM or maybe 1:45 pm."

# \d{1,2} : 1 ya 2 digits hour
# :\d{2} : colon aur 2 digit minutes
# (AM|PM|am|pm) : time format
pattern = r'\d{1,2}:\d{2}\s?(AM|PM|am|pm)'

times = re.findall(pattern, text)
print(times)
# 12-hour time formats ko extract karta hai

text = "Files: report.pdf, image.png, data.csv, notes.docx"

# \.\w+ : dot ke baad file extension
extensions = re.findall(r'\.\w+', text)
print(extensions)
# File extensions ko identify karta hai


import re

text = "Emails: test@gmail.com, invalid@.com, user_123@yahoo.com"

pattern = r'\b\w+@\w+\.(?:com|net|org)\b'

emails = re.findall(pattern, text)
print(emails)  # ['test@gmail.com', 'user_123@yahoo.com']


text = "Phone: 0300-1234567, +92-300-1234567, 0345.7654321"

pattern = r'(?:\+92|03)\d{2}[-.]\d{7}'

phones = re.findall(pattern, text)
print(phones)  # ['0300-1234567', '+92-300-1234567', '0345.7654321']


text = "Meeting at 08:30 AM or maybe 1:5 pm."

pattern = r'\d{1,2}:\d{1,2}\s?(?:AM|PM|am|pm)'

times = re.findall(pattern, text)
print(times)  # ['08:30 AM', '1:45 pm']
