m="Python is a powerful programming language"
n=m.split()
largest=0
for i in range(len(n)):
    if len(n[i])>len(n[largest]):
        largest=i
print(n[largest])
        
