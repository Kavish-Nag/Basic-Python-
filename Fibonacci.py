n= int(input("Generate how many numbers?: "))
a = 0
b = 1
i = 0
print(a)
print(b)
while i<n:
    sum=a+b
    a=b
    b=sum
    i+=1
    print(sum)
