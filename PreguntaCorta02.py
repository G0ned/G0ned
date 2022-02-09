for i in range(1,5):
    if i % 2 == 0:
        for j in range(1,5):
            if j % 2 == 1: 
                print("B ", end = " ")
            else:
                print("N ", end = " ")
    else:
        for j in range(1,5):
            if j % 2 == 1:
                print("N ", end = " ")
            else:
                print("B ", end = " ")
    print()    
