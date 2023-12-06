import sys

def single_calibration(low, high):
    return (high * 10)+low

# TODO I think this should be a lambda
def convert_intermediate_val(intermediates, index):
    # assumes valid input
    return int(intermediates[index].strip('\n'))

# arg 1 input, 2 intermediate (numbers per line), 3 total
with open(sys.argv[1], "r") as f:
    data = f.readlines()

# TODO helper
with open(sys.argv[2], "r") as f:
    intermediate = f.readlines()

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
        low = int(stack.pop())
        high = int(stack[0])
        #print(stack.pop())
        #print(stack[0])
        cal = single_calibration(low, high)
        intermediate_value = convert_intermediate_val(intermediate, data.index(line))
        print(cal == intermediate_value)
    except IndexError:
        pass
