# Using MD5 to store a password hash (insecure)
import hashlib

def store_password_md5(password):
    hash_value = hashlib.md5(password.encode()).hexdigest()
    print(f"Password hash stored as: {hash_value}")

user_password = input("Enter your password: ")
store_password_md5(user_password)
