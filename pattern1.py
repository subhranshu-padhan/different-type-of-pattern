rows=int(input("enter how many rows you want?  "))
for i in range (rows+1):
    for j in range (i):
        print(j+1, end=' ')
    print(' ')
