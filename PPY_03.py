# task 1
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_list = [i*i for i in list1]
print(list1)
print(squared_list)

# task 2

def squared(start, end):
    res = []
    for i in range(start, end + 1):
        res.append(i**2)
    return res

print("task2: ", squared(1, 10))



