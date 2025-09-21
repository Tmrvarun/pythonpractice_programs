# str="we!@$#9lcom@2e"
# new=""
# for x in str:
#     if x.isalpha():
#         new=new+x
#
# print(new) #welcome



str = "we!@$#9lcom@2e"
new = ""
for x in str:
    if x.isalnum():
        new = new + x

print(new) #we9lcom2e
