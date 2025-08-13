# 🔹 TITLE: Change Directory

import os

# os.chdir(path) ka use current working directory ko kisi doosri location pe change karne ke liye hota hai.
# Yahan pe hum 'C:\\Users' (example path) mein ja rahe hain.
os.chdir("C:\\Users")
print("New Working Directory:", os.getcwd())

# 🔹 TITLE: List All Files and Folders

import os

# os.listdir(path) method se hum kisi bhi folder ke andar mojood tamam files aur subfolders ko dekh sakte hain.
items = os.listdir('D:\\Saif A12\\Alarms\\projects py\\jon')
print("Items in Directory:", items)

print(os.getcwd)