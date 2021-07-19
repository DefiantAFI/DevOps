def append(list, number):
    i = 0
    while i < number:
        print(f"At the top i is {i}")
        list.append(i)
        i += 1
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
    return list

num = 6
numbers = []
numbers = append(numbers, num)
print("The numbers: ")

for num in numbers:
    print(num)
