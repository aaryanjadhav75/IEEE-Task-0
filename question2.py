

def process_list(numbers):

    new_list = numbers.copy()

   
    i = 0
    while i < len(new_list):
        if new_list[i] < 0:
            new_list.pop(i)
        else:
            i += 1

   
    new_list.append(0)

   
    new_list.sort()

   
    return new_list



numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


result = process_list(numbers)


print("Original list:", numbers)
print("Processed list:", result)
