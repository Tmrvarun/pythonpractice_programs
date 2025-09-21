lst1=[1,2,5,7,9,1]
lst2=[2,6,8,4,5]

common=[]
for x in lst1:
    if x not in lst2:
        common.append(x)

print(common)


