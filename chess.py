while True:
    cmd=input("Enter your turn:")
    if cmd[0]=='a' or  cmd[0]=='A' or  cmd[0]=='c' or  cmd[0]=='C' or  cmd[0]=='e' or cmd[0]=='E' or  cmd[0]=='G' or  cmd[0]=='g':
        if int(cmd[1]) in range(1,9):
            if int(cmd[1])%2==0:
                print("Its a white space.")  
            else:
                print("Its a black space")
        else:
            print("Invalid block")
    elif cmd[0]=='b' or  cmd[0]=='B' or  cmd[0]=='d' or  cmd[0]=='D' or  cmd[0]=='f' or cmd[0]=='F' or  cmd[0]=='h' or  cmd[0]=='H':
        if int(cmd[1]) in range(1,9):
            if int(cmd[1])%2==0:
                print("Its a black space.")
            else:
                print("Its a white space")
        else:
            print("Not valid Number.")
    else:
        print("Invalid block")
