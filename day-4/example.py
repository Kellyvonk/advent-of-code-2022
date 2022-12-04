r = list(range(5, 18))

print(r)



#######################################

l1 = [4,5,6,7,8]
l2 = [6,7,8,9]

def how_many_are_greater_than_five(l: list):
    i = 0
    for item in list:
        if item > 5:
            i += 1
    return i
    
def all_gt_five(l: list):
    for item in l:
        if item < 5:
            return False
    
    return True

foo = True
for item in l2:
    if item < 5:
        foo = False

print("are all elements in l1 greater than 5?", all_gt_five(l1))
print(f"are all elements in l2 greater than 5? {foo}")