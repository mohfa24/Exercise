
myString = input("input a sentences: ")
items = myString.split(' ')
print(items)

for item in items :
    print(item[0], end='  ')
