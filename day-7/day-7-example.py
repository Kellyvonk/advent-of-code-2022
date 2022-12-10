input1 = open ('input_example', 'r').read()

list_folder = []
totals = dict()
total = 0

def roaldlist(list_folder: list) -> str:
    key = ""
    for folder in list_folder:
        key += folder
    return key



print ("-----------------------------------")

for x in input1.split("\n"):
    if x[0] == '$':
        print ("The command is: ", x)
        if x[2:4] == 'cd':
            folder = x[5:]
            if x[5:] == '..':
                list_folder.pop()
                # print ("The new list is: ", list_folder)
            else:
                list_folder.append(folder)
                totals[roaldlist(list_folder)] = 0
                # print ("The new list is: ", list_folder)
                # print ("The command is: going to", list_folder[-1:])
        else:
            print ("The files in folder", list_folder, "are: ")
    else:
        if x.startswith("dir"):
            print ("We found a 'dir'. ")
            
        else:
            # print ("File : ", x.split(" ")[-1])
            size = int(x.split(" ")[0])
            print ("The file size is :", size, list_folder)

            for i in range(len(list_folder)):
                totals[roaldlist(list_folder[0:i+1])] += size

print ("The total size is: ", totals)

for k in totals.values():
    if k < 100000:
        total += k
    else:
        pass

print ("The sum of size <100000 is: ", total)