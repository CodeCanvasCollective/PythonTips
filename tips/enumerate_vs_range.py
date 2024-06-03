sequence = [ "A", "Z", "C", "F", "D", "B"]

# Traditional way
print('### Traditional way ###')
for i in range(len(sequence)):
    value = sequence[i]
    print(i, value)

print('\n')

# Using enumerate
print('### Using enumerate ###')
for i, value in enumerate(sequence):
    print(i, value)

print('\n')