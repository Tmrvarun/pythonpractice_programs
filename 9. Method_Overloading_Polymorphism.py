# Overloading: We cant achieve this in python directly , if we give more parameters than the passed ones , error will appear , we use none concept and loops concept for each parameter condition
# When we use same method with different parameters passed, we call it overloading of a method
# This can be achieved by Polymorphism,Which means in many forms. eg: Shape- Circle, square and rectangle



# class name():
#     def prt(self,name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
#
# nobj=name()
# # nobj.prt("Jack Smith") #Since we passed value name so if statement gets true and Hello Jack Smith gets printed
# nobj.prt() # Since name is none then else statement is true so only Hello gets printed
#So from above example we came to know that overloading occur if we pass more parameters in the function , but in python we cant achieve it , so we apply if else condition above




# class sum():
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# sobj=sum()
# sobj.add()  #output is 0 as no values were passed
# sobj.add(10,20,30) #output is 60 as three values were passed
# sobj.add(100,300)   #output is 400 as two values were passed
