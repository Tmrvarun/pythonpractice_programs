str="My name is varun"
lst1=list(str) #convert string to list

lst1[3],lst1[6]=lst1[6],lst1[3] # swapping the characters of word name
lst1[11],lst1[15]=lst1[15],lst1[11] ## swapping the characters of word varun
swapped="".join(lst1) #Join the list back into a string
print('swapped string is: ',swapped) #swapped string is:  My eamn is naruv