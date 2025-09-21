from bdb import Breakpoint
from operator import truediv

lst1=[1,5,7,2,4,5,6,7]
lst2=[11,23,7,19]
common=[]


for x in lst1:
    if x in lst2:
        common.append(x)

print(common)





