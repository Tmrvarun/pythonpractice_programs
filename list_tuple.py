# List:
# These are collection of data types
# # lists are indexed ordered and mutable , items can be added removed and modified
# Denoted by []

# mylist=['apple','banana','cherry'] #apple is zeroth element banana is first and cherry is third
# print(mylist) #['apple', 'banana', 'cherry'] #ordered output i.e. output order remains the same everytime
# print(mylist[1]) #banana


# mylist=['apple','banana','cherry','grapes','mango']
# for i in mylist:
#     print(i) #prints all elements

#adding items in list

# mylist=['apple','banana','cherry','grapes','mango']
# mylist.append('Guava')
# print(mylist)  #adds 'Guava' to the end ['apple', 'banana', 'cherry', 'grapes', 'mango', 'Guava']

# mylist=['apple','banana','cherry']
# mylist.insert(1,'Litchi')
# print(mylist) #adds litchi to index no. 1 ,['apple', 'Litchi', 'banana', 'cherry']

#Removing items from list

# mylist=['apple','banana','cherry']
# mylist.pop(2)
# print(mylist) #['apple', 'banana'] removes cherry

# mylist=['apple','banana','cherry']
# mylist.remove("cherry")
# print(mylist) # removes cherry ,['apple', 'banana']

#ADDING TWO LISTS

# mylist=['apple','banana','cherry']
# mylist2=['grapes', 'mango', 'Guava']
# mylist3=mylist+mylist2
# print(mylist3) #['apple', 'banana', 'cherry', 'grapes', 'mango', 'Guava']

# mylist=['apple','banana','cherry']
# mylist2=['grapes', 'mango', 'Guava']
# for i in mylist2:
#     mylist.append(i) #['apple', 'banana', 'cherry', 'grapes', 'mango', 'Guava']
# print(mylist)

#check if item is present in a list

# mylist=['apple','banana','cherry']
# if 'Banana' in mylist:
#     print('banana is present')
# else:
#     print("banana is not present")

# mylist=['apple','banana','cherry']
# mylist[2]="Kela"
# print(mylist) # ['apple', 'banana', 'Kela']





# TUPLE:
# This is indexed and organized collection of data
# Denoted by ()
# They are immutable, they can not be modified , edit ,delete, append etc


# mytuple=("apple","banana","cherry")
# print(mytuple)



# mytuple=("apple","banana","cherry")
# print(mytuple[0],mytuple[2]) # apple cherry



# mytuple=("apple","banana","cherry")
# for i in mytuple:
#     print(i)


# mytuple1=("apple","banana","cherry")
# mytuple2=("pink","yellow","red")
# mytuple=mytuple2+mytuple1 #o/p ('pink', 'yellow', 'red', 'apple', 'banana', 'cherry')
# print(mytuple)


# mytuple1 = ("apple", "banana", "cherry")
# if "cherry" in mytuple1:
#     print("Cherry is present")
# else:
#     print("cherry not present")



#Tuples can be modified if we convert tuple to list first

# mytuple1 = ("apple", "banana", "cherry") #we have to convert a tuple to list in order to modify ,append or add any item
# lst=list(mytuple1)
# lst.append("Guava")
# print(lst) #['apple', 'banana', 'cherry', 'Guava']
# lst.insert(4,"Peach")
# print(lst) #['apple', 'banana', 'cherry', 'Guava', 'Peach']



