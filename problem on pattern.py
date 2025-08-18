star = int(input("star:"))
line = int(input("line:"))
block = int(input("block:"))
for i in range(block):
    c = 0
    for j in range(line-i):
        for k in range(star):
            print("*",end=" ")
            c=c+1
        print()
    print(c)
    print("------------")
