# 🔸 Title: Basic Raise Exception Example
# 🔸 Use: Jab aap chahte hain ke koi specific condition par error generate ho

age = 5

if age < 0:
    raise ValueError("Age cannot be negative!")  # ❌ Manually error uthaya jaa raha hai
else:
    print('Your age is ', age)

    # 🔸 Title: Handling Exception with Try-Except
# 🔸 Use: `raise` ke sath `try-except` use karke program ko crash hone se bachaya jaata hai

try:
    salary = int(input("Enter your salary: "))
    if salary < 10000:
        raise Exception("Salary is too low!")  # ❌ Error throw kiya
    print("Your salary is valid.")
except Exception as e:
    print("Error:", e)  # ✅ Error catch kiya aur custom message diya


    # 🔸 Title: Custom Exception Class
# 🔸 Use: Jab aap apna khud ka error type banana chahein

class InvalidPasswordError(Exception):
    """Custom exception for invalid passwords"""
    pass

password = input('Enter your password')

if len(password) < 6:
    raise InvalidPasswordError("Password must be at least 6 characters long!")  # ✅ Custom error uthaya
else:
    print('Your password is valid')

# 🔸 Title: Function ke andar raise use karna
# 🔸 Use: Kisi input ko validate karna function ke andar

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")  # ❌ Prevented crash
    return x / y

try:
    result = divide(10, 0)
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)

