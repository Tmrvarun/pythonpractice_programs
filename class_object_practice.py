# class name:
#     def text(self):
#         pass
#     def nameprint(self):
#         print("The name is Here")
#
# nm=name()
# nm.text()
# nm.nameprint()


# class name:
#     def text(self):
#         print("Test")
#
#     def text1(self,name):
#         print(name)
#
# nm=name()
# nm.text()
# nm.text1("Varun")


class name:
    def text(self):
        print("Test")
    @staticmethod
    def text1(self,name):
        print(self,name)

nm=name()
nm.text()
name.text1("Varun","Tomar")


# Global and local variable with different names


# i,j=10,20  #Global variable
# class name:
#     a,b=25,15 #class variable
#     def text(self,x,y):
#         print(x+y) #Local variable
#         print(self.a+self.b)
#         print(i+j)
# nm=name()
# nm.text(100,200)


# Global and local variable with same name

# a,b=10,20  #Global variable
# class name:
#     a,b=25,15 #class variable
#     def text(self,a,b):
#         print(a+b) #Local variable
#         print(self.a+self.b)
#         # print(globals()['a']+globals()['b'])  to access global variable we use this syntax
#
# nm=name()
# nm.text(100,200)
