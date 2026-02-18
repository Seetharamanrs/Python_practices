l=[34,56,78,12,36,-5,-45,2]

for i in range(len(l)):
    mini=i
    for j in range(i+1,len(l),1):
        mini=j
    l[i],l[mini]=l[mini],l[i]

print(l[-2])






