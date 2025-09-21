str="dad as sad as mad"
my_dict={}

for x in str:
    if x in my_dict:
        my_dict[x]=my_dict[x]+1

    else:
        my_dict[x]=1

print(my_dict)

max_count=0
m_chr=None

for char,count in my_dict.items():
    if count > max_count:
        max_count=count
        m_chr=char

print("Maximum occurring letter is: ",m_chr)
print("Frequency is: ",max_count)