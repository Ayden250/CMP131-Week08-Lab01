store= int(input("enter number of stores: "))
for i in range(0,store):
    sales=int(input("enter todays.."+str((i+1))+":"))
    sales= sales/100
    for j in range(sales):
        Ast= Ast+"*"
    Ast= Ast+"\n"
