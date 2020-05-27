s=input("Enter number seperated by space")
l=s.split()
t=tuple(l)
x=input("Enter number to find occurence")
count=0
for ele in t:
	if ele==x:
	   count=count+1
print(count)
