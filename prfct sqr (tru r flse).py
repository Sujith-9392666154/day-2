num=int(input("Enter a positive integer: "))
base=1
while num/base!=base:
    base=base+1
if (num/base)%1==0:
    print(num,"is a square")
else:
    print(num,"is not a square")
