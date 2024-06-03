print('\nBuilt-in Function `zip`\n')

names = ['Simon', 'Jonathon', 'Bob']
ages = [25, 30, 35]

# Initialize the zip object for the loop
name_age_zip = zip(names, ages)

print('\n')

for name, age in name_age_zip:
    print(f'{name} is {age} years old')

print('\n')

# Output:
# Simon is 25 years old
# Jonathon is 30 years old
# Bob is 35 years old

# Additional Code

# Initialize the zip
name_age_zip = zip(names, ages)

# It's better to store the list conversion to reuse the zip contents
name_age_list = list(name_age_zip)

# Printing the zip object (this will just print the memory location)
print(name_age_zip)

# Printing the list conversion of the zip object
print(name_age_list)
# Output: [('Simon', 25), ('Jonathon', 30), ('Bob', 35)]

# Display as the list
print(tuple(name_age_list))
# Output: (('Simon', 25), ('Jonathon', 30), ('Bob', 35))

print('\n')
