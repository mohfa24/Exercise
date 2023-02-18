
myString = input("input a sentences: ")
items = myString.split(' ')
print(myString.split(' '))

for item in items :
    print(item[0], end='  ')
