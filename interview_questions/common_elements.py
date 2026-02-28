def common_ele(a,b):
    c=list()
    for i in a:
        if i in b:
            c.append(i)
    return c


a=[1,2,3,4,5]
b=[3,4,5,6,7,8]
# a=['allow','habit','light','python']
# b=['question','allow','green','glow', 'mouse','habit']

print(common_ele(a,b))




