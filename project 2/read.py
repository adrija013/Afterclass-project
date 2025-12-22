
filename = "example.txt"


try:
    with open(filename, "r") as file:
        content = file.read()
        print("Read mode content:")
        print(content)
except FileNotFoundError:
    print("File not found for read mode.")


with open(filename, "w") as file:
    file.write("This file is opened in write mode.\n")
print("Data written using write mode.")


with open(filename, "a") as file:
    file.write("This line is added using append mode.\n")
print("Data appended using append mode.")


with open(filename, "r+") as file:
    print("Read and write mode content:")
    print(file.read())
    file.write("Added using read and write mode.\n")

with open("newfile.txt", "w+") as file:
    file.write("Opened in write and read mode.\n")
    file.seek(0)  
    print("Write and read mode content:")
    print(file.read())


with open("appendfile.txt", "a+") as file:
    file.write("Opened in append and read mode.\n")
    file.seek(0)
    print("Append and read mode content:")
    print(file.read())
