#linear search using functions
def linear(l,target):
    index = 1
    for i in l:
        if i == target:
            return "the value has been found at index: " + str(index)
        index += 1
    return "Not Found"

len = int(input("Enter the length of the list: "))
l = []
for i in range(len):
    l.append(int(input("Enter the value: ")))
target = int(input("Enter the target value: "))
result = linear(l,target)
print(result)
