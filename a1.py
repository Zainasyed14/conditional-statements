ov = float(input("Enter original value : "))
sp = float(input("Enter selling price : "))
if sp>ov :
    print("it is a profit")
    profit=sp-ov 
    print("Profit is" , profit)
else:
    print("it is a loss")
    loss=ov-sp
    print("Loss is" , loss)