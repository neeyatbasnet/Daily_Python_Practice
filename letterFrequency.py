str=input("Enter a string:")
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
for key in dict:
    print(key,':',dict[key])