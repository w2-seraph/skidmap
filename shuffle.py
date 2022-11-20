import random

file = input("Enter file to shuffle: ")

with open(file, 'r') as source:
    data = [(random.random(), line) for line in source]
data.sort()
with open(file, 'w') as target:
    for _, line in data:
        target.write(line) 
print(f"Done shuffling {file}")
