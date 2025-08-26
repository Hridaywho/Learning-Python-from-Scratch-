import os

# Specify the directory path (current directory in this example)
directory_path = '/'
# Use "." for the list of all files in this present folder
# Use ".." for the list of all files in the parent folder
# Use "/" for the list of all files in the root folder like "c drive" in windows
# List all files and directories in the specified path
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
# Note: Make sure you have the necessary permissions to access the specified directory.