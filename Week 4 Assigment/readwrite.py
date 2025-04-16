# Task 1
# This program reads a file
# It also writes a modified version of to a new file
# Modification done is reversing the content and making them upper case

# Read the original content
with open("input.txt", 'r') as f:
    lines = f.readlines()

# Modify the content- reverse each line)
modified_lines = lines[::-1]

# Write the modified content to a new file
with open("output.txt", 'w') as outfile:
    outfile.writelines(modified_lines)

# Success message
print(f"✅ New file has been created with modified content.")