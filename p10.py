# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is some content.\n")
print("File writing complete.")

# Reading from the file
with open("example.txt", "r") as file:
    contents = file.read()
print("File contents:")
print(contents)
