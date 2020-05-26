l1=[]
n=int(input("enter the limit"))
for i in range(0,n):
    items=int(input("enter the element:"))
    l1.append(items)
l2=set()
l3=[]
for i in l1:
    if i not in l2:
            l3.append(i)
            l2.add(i)
print(l3)
