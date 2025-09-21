# lst=[1,5,7,9,12,43,14]
# large1=1
# large2=1
#
# for i in lst:
#     large1=i
#     if large2>large1:
#         large1=large2
#     elif large1>large2:
#         large2=large1
#
# print("first largest: ",large1)

#to find duplicate elements of a list
lst=[1,2,4,5,2,4,7,8,2,4]
dup=[]
count=0

for i in range(1,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]==lst[j] and lst[i] not in dup:
            dup.append(lst[i])

print(dup) #[2, 4]






