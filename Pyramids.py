while True:
    print("MENU")
    print("1. Half Pyramid","\n","2. Inverted Half pyramid","\n","3. Hollow Half Pyramid",
          "\n","4. Full pyramid","\n","5. Hollow Full pyramid","\n","6..Hollow Inverted Half pyramid","\n","7.Exit ")
    ch=int(input("Enter choice:"))
    if ch==1:
        a=int(input("Enter number of elements u want:"))
        rows = a
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print(j ," ",end="")
            print()
    elif ch==2:
        a=int(input("Enter number of elements u want:"))
        rows = a
        for i in range(rows, 0, -1): 
            for j in range(1, i+1): 
                print(j, " ", end="")
            print()  
    elif ch==3:
        a=int(input("Enter number of elements u want:"))
        rows = a
        for i in range(1, rows + 1):  
            for j in range(1, i + 1):  
                if j == 1 or j == i or i == rows:
                    print(j, " ", end="")  
                else:
                    print("  ", end="")  
            print()  
    elif ch==4:
        a=int(input("Enter number of elements u want:"))
        rows = a
        for i in range(1, rows + 1):
            for s in range(rows - i):
                print(" ", end=" ")
            for j in range(i, 2 * i):
                print(j, end=" ")
            for j in range(2 * i - 2, i - 1, -1):
                print(j, end=" ")
            print() 
    elif ch==5:
        n=int(input("Enter number of elements u want:"))
        for i in range(1, n+1):
            print(" " * (n - i), end="")
            for j in range(1, i + 1):
                if j == 1 or j == i or i == n:
                    print(j, end=" ")
                else:
                    print(" ", end=" ")
            print()     
    elif ch==6:
        a=int(input("Enter number of elements u want:"))
        rows = a
        for i in range(rows, 0, -1):
            for j in range(1, i + 1):
                if j == 1 or j == i or i == rows: 
                    print(j, end=" ")
                else:
                    print(" ", end=" ")  
            print() 
    else:
        exit()

        


