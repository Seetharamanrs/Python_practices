def largest_numbers(n):
    largest_number=n[0]
    for num in n:
        if num > largest_number:
            largest_number=num
    return(largest_number)

numbers=[10,20,20,40,50,60]
print("Largest number is ",largest_numbers(numbers))