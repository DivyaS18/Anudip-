#to determine profit or loss 
cp= float(input("Enter the cost price(in Rs): "))
sp= float(input("Enter the selling price(in Rs): "))
if(cp<0):
    print("cost price is invalid")   #checking cost price to be positive
elif(sp<0):
    print("selling price is invalid")   #checking selling price to be positive
else:
    #determining proft and loss
    if(sp > cp):
        print("Profit : Rs ",(sp-cp))
    elif(cp > sp):
        print("profit : Rs ",(cp-sp))
    else:
        print("no profit no loss")
    
