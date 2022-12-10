input = open ('input', 'r').read()

list_folder = []
totals = dict()
total = 0

def roaldlist(list_folder: list) -> str:
    key = ""
    for folder in list_folder:
        key += folder
    return key

for x in input.split("\n"):
    if x[0] == '$':
        if x[2:4] == 'cd':
            folder = x[5:]
            if x[5:] == '..':
                list_folder.pop()
            else:
                list_folder.append(folder)
                totals[roaldlist(list_folder)] = 0
        else:
            pass
    else:
        if x.startswith("dir"):
            pass            
        else:
            size = int(x.split(" ")[0])
            for i in range(len(list_folder)):
                totals[roaldlist(list_folder[0:i+1])] += size

print ("The total size is: ", totals)

for k in totals.values():
    if k < 100000:
        total += k
    else:
        pass

print ("The sum of size <100000 is: ", total)

print ("-------------------PART 2-----------------------")
k = []
for l in totals.values():
    if l > 30000000 - (70000000 - totals['/']):
        k.append(l)
print ("The folder that could be deleted to make enough space is: ", min(k))