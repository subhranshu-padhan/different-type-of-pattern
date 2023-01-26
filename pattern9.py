# n= 5
# for i in range(n):
#     for j in range (i+1):
#         print(1,end="")
#     print("\n")

def printpattern(n):
    s="1"
    for i in range (n):
        print(s)
        s=s+"1"
print(printpattern(6))