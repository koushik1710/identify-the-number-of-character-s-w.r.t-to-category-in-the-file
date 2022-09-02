f=open("demo.txt",'r')
data=f.read()
lowercase_count=0
uppercase_count=0
digits_count=0
specialchars_count=0
for i in data:
    if i.islower():
        lowercase_count+=1

    elif i.isupper():
        uppercase_count+=1

    elif i.isnumeric():
        digits_count+=1

    else:
        specialchars_count+=1



    
print("number of lowercase:-",lowercase_count)
print("number of uppercase:-",uppercase_count)
print("digits:-",digits_count)
print("special character:-",specialchars_count)



f.close()