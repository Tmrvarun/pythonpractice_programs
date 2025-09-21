# s="welcome"
# S=str() #This will initialize a blank string
# # s=str("Welcome") #another way of string
# from multiprocessing.connection import address_type

#Strings are immutable that means they cant be modified and if stored in same variable then it will have different addresses


# print(id(s)) will print the address of string where the string is stored


# string trim: s[0:3] , the first 0 represent from where the trim will start, it includes first value and second value 3 represents the value where the trim will end it takes first string value as 1 and last character is not printed


# s="welcome"
#
# print(s[0:3]) #o/p : wel
#
# print(s[1:6]) #o/p: elcom
#
# print(s[0:-1]) #o/p: welcom it will remove last character from string
#
# print (s[2:-2]) #o/p lco

#+ and * in strings
#
# s='welcome'
# s1=' To python'
# # print(s+s1) welcome To python
# # print(s*3) welcomewelcomewelcome

# # relational strings:
#
# print("TESTER">="testr")
# print('still'=='still')
# print('Try'<'TRY')
# print('list'!='List')



# s='welcome'
# s1='to python'
#
# print(s1.capitalize()) #To python
# print(s1.islower())
# print(s.title()) #Welcome , prints first letter as capital
# print(s1.title())
# print(s1.endswith("thon"))
# print(s.swapcase()) #WELCOME upper case to lower and vice versa

#String swap
#
# s="welcome"
# # ety=""
# # for i in s:#here strings last char is assigned to i and loops runs
# #     ety=i+ety
# # print("Reversed string is: ",ety)
#
#
# print(s[::-1]) #first two blank means it starts from 0-w  and till last char-e, -1 will take last and print each character each time