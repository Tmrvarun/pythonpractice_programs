str="nitin is lier"
rev_str=""

for i in str:
    rev_str=i+rev_str

if str==rev_str:
    print("Palindromic")
else:
    print("Not palindromic")

print("Reversed string is: ",rev_str) #Reversed string is:  reil si nitin