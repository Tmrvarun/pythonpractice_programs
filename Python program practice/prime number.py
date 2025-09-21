num=6
count=0

if num>1:
    for i in range (1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print(" Prime number")
    else:
        print("Not prime number")

