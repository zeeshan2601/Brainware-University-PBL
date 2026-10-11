#write a program in python to calculate teh difference between max and min value in a given list using loop

def diff_max_min(l):
    max_value = l[0]
    min_value = l[0]
    for i in l:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i
    return max_value - min_value    

n = int(input("Enter the length of the list: "))
l = []
for i in range(n):
    l.append(int(input("Enter the value: ")))
result = diff_max_min(l)
print("The difference between max and min value in the list is:", result)
