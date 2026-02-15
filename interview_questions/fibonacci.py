def fibonnaci_series(n):
    d=[]
    i=0
    j=1
    for _ in range(0,n):
        d.append(i)
        tot=i+j
        i,j=j,tot
    return(d)
while True:
    try:
        n=int(input("Enter the number: "))
        if n==0:
            print(0)
        elif n<=0:
            print("Invalid number")
        break
    except ValueError:
        print("Enter the number please!")
print(fibonnaci_series(n))