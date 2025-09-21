lst=[12,34,6,7,9,21,43]
k=len(lst)
print("Length of list is",k)
print("List before swapping",lst)
for i in lst:
    if i==lst[0]:
        j=i
        lst[0]=lst[-1]
        lst[-1]=j
        print("After swapping list:",lst)


