# range(): This function is used to define the range upto which our function will run , instead of writing multiple prints we use range functions with for loop
#
#
# range(10): will print values starting from 0 to 10-1 =9.

# print(list(range (10)))  #o/p : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(list(range(1,10)))   #o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(list(range (1,10,2)))  #o/p:[1, 3, 5, 7, 9] starts from 1 till 9 ,
#
# print(list(range(10,1,-1))) #[10, 9, 8, 7, 6, 5, 4, 3, 2] #starts from 10 and ends till 2 ,as 2 is the last number and range runs till n-1
#
# print(list(range(-10,-1,2))) #[-10, -8, -6, -4, -2] # starts from -10 and ends till -2 as range ends till n-1
#
#

# for loop:
#
# for i in range(10):  #o/p 0 to 9
#     print(i)


# for i in range (1,10,2): #o/p : 1,3,5,7,9
#     print(i)

# for i in range (-10,-5): #o/p : -10 to -6 as range end till n-1
#     print(i)

# type conversion:

# m=input("enter value of m")
# n=input("enter value of n")
#
# # print(m+n) #output : 100200 as it takes both values as strings
#
# print(int(m)+int(n)) #output : 100200
#
# Method 2:

# m=int(input("value of m=: "))
# n=int(input("value of n : "))
# print(m+n) #output : 100200
