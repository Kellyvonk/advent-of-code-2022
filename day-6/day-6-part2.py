input = open ('input', 'r').read()

list_input = list(input)

marker = 0

n = 14

def dupcheck(x):
    for elem in x:
        if x.count(elem) > 1:
            return True
    return False

for i in range(len(list_input)-n+14):
    print ("-----------------------")
    batch = input[i:i+n]
    print ("Window is: ", batch)
    del list_input[0]
    marker = marker+1
    print ("New window is: ", batch)
    if dupcheck(batch):
        print ("There are duplicates.")
    else: 
        print ("No duplicates")
        print ("The marker is: ", marker+13)
        break

