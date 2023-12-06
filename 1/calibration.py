import sys

DIGITS = ["one", "two", "three",
          "four", "five", "six", "seven", "eight", "nine"]

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

output = 0

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
        output+=cal
        intermediate_value = 0# convert_intermediate_val(intermediate, data.index(line))
        print(cal == intermediate_value)
    except IndexError:
        pass

test_answer = 0
#with open(sys.argv[3], "r") as f:
#    data = f.read()
#    data = data.strip('\r')
#    data = int(data)
#    test_answer = data

print("Final answer")
print(output)
match = (output==test_answer)
print(f"Matches test? {match}")
