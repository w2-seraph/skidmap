import sys
import random
import os
# opening the file in read mode

my_file_input = input("Enter keywords file:")
my_file = open(my_file_input, "r")

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

sys.stdout = open('dorks-generated.txt', 'w')

for o in item0:
    for f in item1:
        for s in item2:
            for t in item3:
                print(o + " " + f + "." + s + "?" + t + "=")

sys.stdout = orig_stdout
sys.stdout.write("[+]dorks-generated.txt generated")

os.system(f"sort -u -o dorks-generated.txt dorks-generated.txt")

with open('dorks-generated.txt', "r") as f:
    num_lines = len(f.readlines())
    print(f"\n[+]counted {num_lines} dorks")

sys.stdout.close()

with open('dorks-generated.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('dorks-generated.txt','w') as target:
    for _, line in data:
        target.write( line )

