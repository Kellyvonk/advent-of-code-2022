input = open ('input', 'r').read()

# each line is 1 pair of elves
# 1 pair is splitted with komma
# compare same number within list of number in elves in pairs

def fully_contain(space_elf1: list, space_elf2: list):
    for space in space_elf1:
        if space not in space_elf2:
            return False

    return True

def partial_contain(space_elf1: list, space_elf2: list):
    for space in space_elf1:
        if space in space_elf2:
            return True
    
    return False

fully_contain_list = []
partial_contain_list = []

for elves in input.split("\n"):
    elves = elves.split(',')

    [nums_elf1a, nums_elf1b] = elves[0].split('-')
        
    elf1 = list(range(int(nums_elf1a), int(nums_elf1b)+1))

    [nums_elf2a, nums_elf2b] = elves[1].split('-')

    elf2 = list(range(int(nums_elf2a), int(nums_elf2b)+1))

    if fully_contain(elf1, elf2) or fully_contain(elf2, elf1):
        fully_contain_list.append(True)    

    if partial_contain(elf1, elf2) or partial_contain(elf2, elf1):
        partial_contain_list.append(True)

print (fully_contain_list)

all_true = fully_contain_list.count(True)
print ("The number of fully contained elves are: ", all_true)

print (partial_contain_list)

partial_true = partial_contain_list.count(True)
print ("The number of partial contained elves are: ", partial_true)

