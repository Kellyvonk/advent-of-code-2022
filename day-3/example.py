alpha = "#abcdefg"

print('a' in alpha)
print(alpha.index('a'))
print(alpha.index('c'))

for a in alpha:
    if a == 'a':
        print(1)
    if a == 'b':
        print(2)
    # etc...