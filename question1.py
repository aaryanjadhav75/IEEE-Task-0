

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)
largest = numbers[0]
smallest = numbers[0]

total = 0
even_count = 0
odd_count = 0

for num in numbers:

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    total += num

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

reverse_list = []

for i in range(n - 1, -1, -1):
    reverse_list.append(numbers[i])

print("\n--- List Analysis ---")
print("Largest element:", largest)
print("Smallest element:", smallest)
print("Sum of all elements:", total)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
print("List in reverse order:", reverse_list)
