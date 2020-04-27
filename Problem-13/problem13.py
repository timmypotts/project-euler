filename = 'p13.txt'

with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
print(array)

newArray = []

for i in array:
    j = i.rstrip('\n').split(",")
    k = [int(n) for n in j]
    f = k.pop()
    newArray.append(f)


arraySum = sum(newArray)
print(str(arraySum)[:10])
