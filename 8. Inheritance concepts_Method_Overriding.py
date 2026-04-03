# 1)  Single Inheritance: it has single parent and single child , child inherits all variables and methods here

# class A():
#     def m1(self):
#         print("This is class from parent")
#
# class B(A):
#     def m2(self):
#         print("This is class from child")
#
# bobj=B()
# bobj.m2()
# bobj.m1()

# Single inheritance with parameters:

# class A:
#     a,b=10,20
#     def m1(self):
#         print(self.a + self.b)
#
# class B(A):
#     x,y=300,200
#     def m2(self):
#         print(self.x - self.y)
#
# bobj=B()
# bobj.m2()
# bobj.m1()



#2) Multilevel inheritance : It has multiple class that acts as parent and child in a sequential form

# class A:
#    a,b=10,20
#    def m1(self):
#        print(self.a + self.b)
#
# class B(A):
#   x,y=300,200
#   def m2(self):
#       print(self.x - self.y)
#
# class C(B):
#     i,j=3,5
#     def m3(self):
#         print(self.i * self.j)
#
# cobj=C()
# cobj.m3()
# cobj.m2()
# cobj.m1()

# 3) Hierarchy inheritance: It has single parent and multiple child

# class A:
#     a,b=10,20
#     def m1(self):
#          print(self.a + self.b)
#
# class B(A):
#      x,y=300,200
#      def m2(self):
#            print(self.x - self.y)
#
# class C(A):
#         i,j=3,5
#         def m3(self):
#           print(self.i * self.j)
#
# cobj=C()
# cobj.m3()
# cobj.m1()
#
# bobj=B()
# bobj.m2()
# bobj.m1()

# 4) Multiple Inheritance: It has multiple parents and a single child

# class A:
#    a,b=10,20
#    def m1(self):
#         print(self.a + self.b)
#
# class B:
#     x,y=300,200
#     def m2(self):
#           print(self.x - self.y)
#
# class C(A,B):
#        i,j=3,5
#        def m3(self):
#          print(self.i * self.j)
#
# cobj=C()
# cobj.m3()
# cobj.m1()
# cobj.m2()

# 5) Overriding : in this we can have same name of methods and can override it , we can override the method name by super() keyword

class A():
    def m1(self):
       print("This is class from parent")

class B(A):
    def m1(self):
       print("This is class from child")
       super().m1()

bobj=B()
bobj.m1()
# #            Output:
#           #This is class from child ,without any super() keyword it prints the latest method value
#           O/P # This is class from child, as print statement falls before super() keyword
#           O/P # This is class from parent, super() keyword statement takes parent m1 statement

# 6) We can override variable of class as well

# class A():
#     name="John"
#     def m1(self):
#        print(self.name)
#
# class B(A):
#     name="Chris"
#     def m1(self):
#        print(self.name) #This will print John ,without super() it will print chris as it will print latest value of name in a class
#
# bobj=B()
# bobj.m1()

# 7) We can inherit variable of a class to other class and use them

# class A:
#    a,b=10,20
#
# class B(A):
#    x,y=300,200
#    def m2(self,i,j):
#         print(self.x - self.y)
#         print(i*j)
#         print(self.a + self.b)
#
# bobj=B()
# bobj.m2(100,200)
