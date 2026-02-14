numbers=[10,20,20,40,50,60]

largest_number=numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number=num
print("largest",largest_number)