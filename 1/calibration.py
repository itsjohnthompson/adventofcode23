import sys

with open(sys.argv[1], "r") as f:
    data = f.readlines()

for line in data:
    chars = line.strip('\n')
    print(chars)
