def longest_words(m):
    n=m.split()
    largest=0
    for i in range(len(n)):
        if len(n[i])>len(n[largest]):
            largest=i
    return n[largest]

# m="Python is a powerful programming language"
while True:
    try:
        m = input("Enter the Sentences: ")
        break
    except ValueError:
        print("Please Enter the Character ")


print(longest_words(m))