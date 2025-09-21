# Set :
# Sets are unordered and unindexed collection of data
# Denoted by {}
# They are mutable
from itertools import pairwise

# myset={"Apple","Banana","Cherry"}
# print(myset) #{'Banana', 'Apple', 'Cherry'} unordered output

# myset={"Apple","Banana","Cherry"}
# for i in myset:
#     print(i)

# myset={"Apple","Banana","Cherry"}
# print(len(myset)) # 3

# myset={"Apple","Banana","Cherry"}
# myset.add("Grapes")
# print(myset) #{'Apple', 'Banana', 'Grapes', 'Cherry'}

# myset={"Apple","Banana","Cherry"}
# myset.update(['pink','blue']) #{'Apple', 'Banana', 'pink', 'blue', 'Cherry'} items added
# print(myset)

# Delete sets :remove , discard

# myset={"Apple","Banana","Cherry"}
# myset.remove("Cherry") #{'Apple', 'Banana'}
# print(myset)
#
# myset={"Apple","Banana","Cherry"}
# myset.discard("Cherry")
# print(myset)

# Join two sets :union

# myset1={"Apple","Banana","Cherry"}
# myset2={"Red","Yellow","Pink"}
# myset=myset1.union(myset2)
# print(myset)

# myset1={"Apple","Banana","Cherry"}
# myset2={"Red","Yellow","Pink"}
# myset1.update(myset2)
# print(myset1) #{'Pink', 'Yellow', 'Cherry', 'Apple', 'Red', 'Banana'}


# Dictionary :
# They are the collection of unindexed, ordered data types
# denoted by {} , uses key value pair
# They are mutable

# mydic={
#     "Brand":"Hyundai",
#     "Model":  '2024',
#     "Name": 'i10'
#
# }
# print(mydic) #{'Brand': 'Hyundai', 'Model': '2024', 'Name': 'i10'}



# mydic={
#     "Brand":"Hyundai",
#     "Model":  '2024',
#     "Name": 'i10'
#
# }
# print(mydic["Name"]) #i10 prints name from mydic


# mydic={
#     "Brand":"Hyundai",
#     "Model":  '2024',
#     "Name": 'i10'
#
# }
# for i in mydic:
#     print(i) #prints all keys
#
# for i,j in mydic.items():
#     print(i,j) #Prints all key and value
#
# for i in mydic.values():
#     print(i) #prints all values of keys


# mydic= {
#     "Brand": "Hyundai",
#     "Model": '2024',
#     "Name": 'i10',
#
# }
# mydic["cOLOUR"]="rED"
# print(mydic) #Adds colour to dictionary



# mydic={
#     "Brand":"Hyundai",
#     "Model":  '2024',
#     "Name": 'i10'
#
# }
#
# mydic.pop("Name")
# print(mydic)
# 
# del mydic["Model"]
# print(mydic)
