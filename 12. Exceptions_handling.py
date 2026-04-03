# Exceptions:
# These are conditions which occur when a user gives wrong input and the following codes does not get executed
# try,except,else and finally are the keywords used for exception
# try except should come together, while : else and finally are optional , finally gets executed always in a code

# Without try and except
# print("This is test code")
# print("Test code is running")
# print(x) #NameError: name 'x' is not defined , since we have not defined x . the below lines not get executed
# print("Test code is compiled")
# print("Test code execution is complete")


# # With try and except : all lines get executed and try block has exception so except gets printed following the below lines
#
# print("This is test code")
# print("Test code is running")
# try:
#     print(x) #NameError: name 'x' is not defined , since we have not defined x . the below lines not get executed
# except:
#     print("Code has some exception")
# print("Test code is compiled")
# print("Test code execution is complete")


# With try , multiple except, else and finally keywords

# print("This is test code")
# print("Test code is running")
#
# try:
#     num=10
#     print(num/2)
#     print("Code executed successfully")
# except ZeroDivisionError:
#     print("There is ZeroDivision error")
#
# except SyntaxError:print("There is SYNTAX error")
#
# except:
#     print("Code has some exception")
#
# else:
#     print("No exception")
# finally:
#     print("This is finally")


# Above code output with value /0 :
#     This is test code
#     Test code is running
#     There is ZeroDivision error , 'else' block is not executed as ZeroDivision occurs
#     This is finally

# Above codes output with value div/2 :
#     This is test code
#     Test code is running
#     5.0
#     Code executed successfully
#     No exception , since there is no exception so 'else' will get executed along with finally block code
#     This is finally


#User defined exception : In this a user add his own exception to deal with human exceptions

def num(n):
    if n<0 :
        raise ValueError ("INTEGER NUMBER IS NEEDED")
    if n%2 == 0 :
        print("Even Number")
    else :
        print("Odd number")

obj=-1
try:
    num(obj)
except ValueError:
    print("Value error handled")

    #In the above code we have added value error , so that if user enters an invalid value then the exception gets handled
    #Suppose a user is using the code of other dev , so he must be able to handle the exceptions to the code
