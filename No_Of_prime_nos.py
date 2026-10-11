def isPrime(n):
    c = 0
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            c += 1
    if c == 0:
        return True
    else:
        return False

def prime_numbers_with_index(lst):
    prime_count = 0
    index = 1
    for i in lst:
        if isPrime(i):
            prime_count += 1
            print(index, end=" ")

        index += 1
    print()
    print(prime_count)

n = int(input("Enter the number of elements in the list: "))
lst = []
for i in range(0,n):
    num = int(input("Enter element "))
    lst.append(num)
prime_numbers_with_index(lst)