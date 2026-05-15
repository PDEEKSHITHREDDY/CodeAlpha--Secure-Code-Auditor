import subprocess
import hashlib
import pickle
import os

# Hardcoded password
password = "admin123"

# Weak hashing
data = "secret_data"
hash_value = hashlib.md5(data.encode()).hexdigest()

# Dangerous subprocess usage
command = input("Enter command: ")
subprocess.call(command, shell=True)

# Unsafe pickle loading
pickle_data = input("Enter pickle file: ")

with open(pickle_data, "rb") as file:
    obj = pickle.load(file)

# Dangerous os command
user_input = input("Enter system command: ")
os.system(user_input)

print("Completed")