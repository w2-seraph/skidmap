import os

os.system("cp dorks_out.txt ./comparison/dorks_out.txt.bak")
os.system("cp ./comparison/big-links-file.txt ./comparison/big-links-file.txt.bak")

os.system(f"wc -l dorks_out.txt\n")

f2 = open("dorks_out.txt", "r")
f1 = open("./comparison/big-links-file.txt", "r")
f4 = open("./comparison/big-links-file.txt", "a")

file1_raw = f1.readlines()
file2_raw = f2.readlines()

result = [x.strip() for x in file2_raw if x not in file1_raw]

print(f"[+]Counted {len(result)} unique urls")


for line in result:
	f3 = open('p0wz.txt', 'a')
	f3.write('\n')
	f3.write(line)

	f4.write('\n')
	f4.write(line)

print("Done appending to big file.")

os.system("wc -l ./comparison/big-links-file.txt")
os.system("mv p0wz.txt dorks_out.txt")
os.system("wc -l dorks_out.txt")
