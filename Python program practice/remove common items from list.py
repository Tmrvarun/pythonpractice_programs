lst1=[1,5,7,9,3,5]
lst2=[2,6,8,3,5]

common=[]

for i in lst1:
    if i not in lst2:
        common.append(i)

print(common)