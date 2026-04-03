# Constructor:
#
# declared as __init__
# Automatically invoked at the time of object creation
# Does not return any value
# Can take parameter


# class constructor:
#
#     def __init__(self):
#         print("This is Constructor")
#
#     def disp(self):
#         print("This is method")
#
# cns=constructor()   # o/p "This is Constructor" as constructor is invoked automatically at object creation
#
# cns.disp()  # o/p "This is method" , to display dsp method we have to call through object


# class const:
#
#     def __init__(self,empid,ename,sal):
#         self.empid=empid  #Instead of defining the variable outside the method we can define it within this method
#         self.ename=ename  # We can access these variable anywhere in the class
#         self.sal=sal
#
#     def dsp(self):
#         print(self.ename)
#         print(self.empid)
#         print(self.sal)
#
#     def __str__(self):  #this constructor is used to print string type variable only
#         return(self.ename)
#
# cn=const(1001,"Varun",1500000)
# cn.dsp()
# print(cn) # this will print the returned value of string type constructor
