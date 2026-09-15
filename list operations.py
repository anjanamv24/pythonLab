numbers = list(map(int, input("Enter elements: ").split()))

print("List:", numbers)

key = int(input("Enter element to search: "))

if key in numbers:
    print("Element found at index:", numbers.index(key))
else:
    print("Element not found")

pos = int(input("Enter position (index): "))
new_val = int(input("Enter new value: "))

if 0 <= pos < len(numbers):
    numbers[pos] = new_val
    print("Updated List:", numbers)
else:
    print("Invalid position")

even_numbers = [x for x in numbers if x % 2 == 0]

print("Even Numbers:", even_numbers)

print("Length of List:", len(numbers))

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)
