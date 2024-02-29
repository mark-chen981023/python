import os

os.listdir()
print()

with open("new_file.text", "w") as F:
    f.write("Hello, Micropython")

print(os.listdir())
os.remove("new_file.text")
print(os.listdir())
