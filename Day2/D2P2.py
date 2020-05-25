N = int(input("Enter the value of N: "))
x = 0
y = 1
print("The Fibonacci series upto", N, "th number is following:")
for i in range(N):
    print(x, end = " ")
    z = x + y
    x = y
    y = z
