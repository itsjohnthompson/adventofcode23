import sys

# arg 1 input, 2 intermediate (numbers per line), 3 total
with open(sys.argv[1], "r") as f:
    data = f.readlines()

for line in data:
    chars = line.strip('\n')
    print(chars)
    
    stack = []
    first_num = True
    for char in chars:
        if char.isnumeric():
            #print(char)
            if first_num:
                first_num = False
                stack.append(char) # In case only one number
            stack.append(char)

    # TODO what if empty?
    try:
        print(stack.pop())
        print(stack[0])
    except IndexError:
        pass
