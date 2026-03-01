
def second_largest():
    for i in range(len(l)):
        mini=i
        for j in range(i+1,len(l),1):
            mini=j
        l[i],l[mini]=l[mini],l[i]

    return l[-2]


l=[34,56,78,12,36,-5,-45,2]

print(second_largest(l))





