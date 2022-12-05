stack_1 = ['B', 'Q', 'C']
stack_2 = ['R', 'Q', 'W', 'Z']
stack_3 = ['B', 'M', 'R', 'L', 'V']
stack_4 = ['C', 'Z', 'H', 'V', 'T', 'W']
stack_5 = ['D', 'Z', 'H', 'B', 'N', 'V', 'G']
stack_6 = ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q']
stack_7 = ['D', 'G', 'T', 'R', 'W', 'Z', 'S']
stack_8 = ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P']
stack_9 = ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P']

list_stacks = [[], stack_1, stack_2, stack_3, stack_4, stack_5, stack_6, stack_7, stack_8, stack_9]

input = open ('input', 'r').read()

for x in input.split("\n"):
    a, end = x.split('to')
    end = int(end)
    c, start = a.split('from')
    start = int(start)
    e, nums_box = c.split('e')
    nums_box = int(nums_box)
    
    for _ in range(nums_box):
        list_stacks[end].append(list_stacks[start].pop())

print ("---------------------- PART 1 -------------------------")
print ("The top letters in crates are: ", list_stacks[1][-1],list_stacks[2][-1],list_stacks[3][-1],list_stacks[4][-1],list_stacks[5][-1],list_stacks[6][-1],list_stacks[7][-1],list_stacks[8][-1],list_stacks[9][-1])

