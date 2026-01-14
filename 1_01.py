num_input = (input("Input : "))
if len(num_input)==1:

    if num_input.isnumeric():
        last =0
        sum = 0
        for i in range(4):
            new = int(num_input)*(10**i)
            newadd = new+last
            last = newadd
            sum = sum+newadd
            
        print(f"Output : {sum}")
    else :
        print("Output : Invalid Input")
else :
        print("Output : Invalid Input")



