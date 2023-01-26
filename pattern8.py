n = 10

for i in range(0, n):
    k = n-i
    for j in range(0, k):
        print(end=" ")

    for j in range(0, i+1):
        print("*", end=" ")

    print("\r")

for i in range(n, 0, -1):
    k = n-i
    for j in range(0, k):
        print(end=" ")

    for j in range(0, i):
        print("*", end=" ")

    print("\r")
