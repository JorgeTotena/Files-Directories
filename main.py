#  HOW TO READ INTO A FILE
"""with open("my_file.txt") as file:  # this way you don't to close the file every time, just need to use with statement
    contents = file.read()
    print(contents)
    #  file.close()  # it's important to close the files to avoid spending unnecessary resources from the computer. """

# HOW TO WRITE INTO A FILE
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text")

