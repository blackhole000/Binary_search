# a function that takes a list and target parameter
# multiple variables: middle, start,end,steps
# recursion pr while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list_fun, element):
    middle = 0
    start = 0
    end = len(list_fun)
    steps = 0
    while start <= end:
        print("Step", steps, ":", list_fun[start:end + 1])

        steps = steps + 1
        middle = (start + end) // 2

        if element == list_fun[middle]:
            return middle
        elif element < list_fun[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

result = binary_search(my_list, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in list")
