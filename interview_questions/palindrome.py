def palindrome(n):
    m=n.lower()
    if m[::-1]==m:
        print("Palindrome")
    else:
        print("Not a Palindrome")

while True:
    n=input("Enter the word")
    palindrome(n)
    break
