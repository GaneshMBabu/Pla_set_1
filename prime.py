num = int (input("Enter the number: "))
if (num>0):
    print("Prime numbers are:")
    for i in range(0,num+ 1):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
                else:
                    print(i)
else:
    print("Enter a valid input ")
