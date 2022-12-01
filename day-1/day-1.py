input = open ('input', 'r').read()


total_calories_elf = 0

calories_elf = input.split("\n\n")
all_totals = []

for calories_nums_elf in calories_elf:
    calories_nums_elf = calories_nums_elf.split("\n")

    total_calories_elf = sum([int(calories) for calories in calories_nums_elf])
    print (total_calories_elf)
    all_totals.append (total_calories_elf)
    print (all_totals)

biggest = max(all_totals)
print (biggest)

all_totals.sort(reverse=True)
print (all_totals)

top_three = all_totals[0:3]
print (top_three)

total_top_three = sum(top_three)
print (total_top_three)