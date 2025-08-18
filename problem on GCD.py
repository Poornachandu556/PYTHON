a = int(input("number1:"))
b = int(input("number2:"))
while(b!=0):
    rem = a%b
    a = b
    b = rem
print(a)
