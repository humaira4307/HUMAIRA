file_path = "example.txt"
file = open(file_path, "r")

content = file.read()
print("File content:")
print(content)
file.close()

file = open(file_path, "w")
file.write("This is a new line.")

file.close()

file = open(file_path, "r")
updated_content = file.read()
print("Updated file content:")
print(updated_content)
file.close()