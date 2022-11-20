import sys
import random
import os

# Will not ask for input and instead use hardcoded keywords.txt

# my_file_input = input("Enter generic wordfile:")
my_file = open('keywords.txt', "r")
print("[+]Using keywords.txt to generate")

fdata = my_file.read()

data_into_list = fdata.split("\n")
my_file.close()

item0 = data_into_list
item1 = ['view', 'user', 'browse', 'photo', 'search'
         , 'file', 'page', 'product', 'offer', 'browse', 'home'
         , 'about', 'index', 'index2', 'default', 'faq', 'main']
item2 = ["php", "asp"]
item3 = ['id', 'cid', 'page', 'cat', 'page_id']

orig_stdout = sys.stdout

sys.stdout = open('dorks-static.txt', 'w')

for o in item0:
    for f in item1:
        for s in item2:
            for t in item3:
                print(o + " inurl:" + f + "." + s + "?" + t + "=")

sys.stdout = orig_stdout
sys.stdout.write("[+]dorks-static.txt generated")

os.system(f"sort -u -o dorks-static.txt dorks-static.txt")

with open('dorks-static.txt', "r") as f:
    num_lines = len(f.readlines())
    print(f"\n[+]counted {num_lines} dorks")
    print("[+]Copying dorks.txt files to main directory...")

sys.stdout.close()

with open('dorks-static.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('dorks-static.txt','w') as target:
    for _, line in data:
        target.write( line )
os.system("split -n 3 dorks-static.txt")
os.system("sed -i '1d' xab")
os.system("sed -i '1d' xac")
os.system("cp xaa ../dorks.txt")
os.system("cp xab ../dorks2.txt")
os.system("cp xac ../dorks3.txt")

