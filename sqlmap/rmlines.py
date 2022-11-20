import os

n = int(input("Enter number of lines to remove: "))
filename = input("Enter file name: ")

nfirstlines = []

with open(filename) as f, open("bigfiletmp.txt", "w") as out:
    for x in range(n):
        nfirstlines.append(next(f))
    for line in f:
        out.write(line)

os.remove(filename)
os.rename("bigfiletmp.txt", filename)
print("Finished removing lines")
