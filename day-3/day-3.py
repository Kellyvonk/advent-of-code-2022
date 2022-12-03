input = open ('input', 'r').read()

print (input)

# first split rucksack into 2 compartments = allcharacters/2
# find the one type that is similar
# convert the type into number
# sum all number from each rucksack
   # item = types in bag1 == types in bag2 

lowercase = "#abcdefghijklmnopqrstuvwxyz"
uppercase = "#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(lowercase.index('a'))
print(uppercase.index('B'))

list = []

for idx, types in enumerate(input.split("\n")):
    print(f"-------- {idx} --------")
    num_types_rucksack = int(len(types) /2)
    print (num_types_rucksack)
    
    bag1 = types[0:num_types_rucksack]
    bag2 = types[num_types_rucksack:]
    print (bag1)
    print (bag2)
    
    for item in bag1:
        if item in bag2:
            print (item)
            if item.isupper():
                list.append(uppercase.index(item))
                break
            if item.islower():
                list.append(lowercase.index(item))
                break
print (sum(list))

grouplist = []
elfs = input.split("\n")

start = 0
end = len(elfs)
step = 3

for i in range(start, end, step):
    groups = elfs[i:i+step]

    elf1 = groups[0]
    elf2 = groups[1]
    elf3 = groups[2]

    for item in elf1:
        if item in elf2 and item in elf3:
            print (item)
            if item.isupper():
                grouplist.append(uppercase.index(item))
                break
            if item.islower():
                grouplist.append(lowercase.index(item))
                break

print (sum(grouplist))
   