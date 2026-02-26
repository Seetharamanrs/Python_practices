

def freq(w1,w2):
    wo1=w1.lower()
    wo2=w2.lower()
    return sorted(wo1)==sorted(wo2)
    
while True:
    try:
        n=input("Enter the first word: ")
        n1=input("Enter the second word: ")
        break
    except ValueError:
        print("Please Enter the Character")
if freq(n,n1):
    print("It's Anagarams")
else:
    print("Not Anagrams")
