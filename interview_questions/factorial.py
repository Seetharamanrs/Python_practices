def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    return(fact)
while True:
    try:
        n=int(input("Enter the number for factorial: "))
        break
    except ValueError:
        print("Enter the number please!")
print(f"Factorial of {n} is ", factorial(n))