# def func():
#     print("This is function")
# func() #function is getting called

# def func(name):
#     print("Hello",name)
#
# func("Smith") #Hello Smith

# def func(a,b):
#     return(a+b)
#
# k=func(100,200)
# print(k) #function takes arguments and return a value

# def func(a,b):
#     print(a+b)
#
# func(100,200) #function takes arguments but return no value

# def func():
#     i=20
#
# print(func()) #None function takes no value and return no value


# x=100
#
# def func():
#     x=20
#     print(x)
#
# print(x) #100 as x is the global variable and x within func is local

#

# arguments:
#
# Positional arguments and keyword arguments

def func(i,j,k):
    print(i+j+k)

func(10,20,30) #positional arguments

func(j=10,i=20,k=25)  #keyword argument

# func(10,j=20,30) #error as we have to declare positional argument before keyword argument
func(10,20,k=30)
