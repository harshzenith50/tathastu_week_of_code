string=input("enter the string to remove duplicate from it")
s1=""
j=0
for i in string:
    if(string.index(i)==j):
        s1=s1+i
        j=j+1 
print(s1)
