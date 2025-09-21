#use dictionary , if else loop

str='dad as sad as dad'

my_dict={} #blank dictionary

for i in str:
    if i in my_dict:
        my_dict[i]=my_dict[i]+1 #this code will add one more character and increase count to dictionary
    else:
        my_dict[i]=1 #this gets initiated first and in this d gets stored and value 1 gets stored first

print(my_dict)


