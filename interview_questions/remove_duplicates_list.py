def remove_duplic(l):
    c=list()
    for i in l:
        if i not in c:
            c.append(i) 
    print(c)



# l=[1,2,2,3,4,5,6,7]
l=['words','allow','allow','habit','light']
remove_duplic(l)