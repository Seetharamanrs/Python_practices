def prime_number(n):
    if n==0 or n==1:
        print("NOT PRIME NUMBER")
    else:
        for i in range(2,n):
            if n%i==0:
                print("NOT PRIME NUMBER")
                break
        else:
            print("PRIME NUMBER")

while True:
    try:
        n=int(input("Enter the number to check prime number: "))
        break
    except ValueError:
        print("Enter the number please!")
prime_number(n)

