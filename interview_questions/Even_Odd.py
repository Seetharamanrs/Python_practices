
def even_odd(n):
    if n%2==0:
        return("EVEN")
    else:
        return("ODD")
while True:
    try:
        n=int(input("Enter the number: "))
        break
    except ValueError:
        print("Enter the number Please! ")
print(even_odd(n))
