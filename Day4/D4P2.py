l= [(4, 5, 1), (6, 1, 5), (7, 4, 2), (6, 2, 4)]
N=int(input("Enter nth element"))
l.sort(key = lambda x: x[N])
print(str(l))
