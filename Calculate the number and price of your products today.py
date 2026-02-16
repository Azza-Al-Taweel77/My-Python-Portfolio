print("\n ***** Welcome to iShop calculator ***** \n")
items= int(input("How many items are there in your basket today? "))
item=[]
your_price=[]
if item > 0:
    print("\nLet's get to counting them .... ")
    for G in range(1,items+1):
        number_items= input(f"Please tell me the name of the item number {G}: ")
        price= float(input(f"What is the price of {number_items} \n$"))
        item.append(number_items)
        your_price.append(price)
    basket_items= input("Would you like to see your entire basket items? ").lower()

    if basket_items == "yes":
        print(item)
        total_price= input("Would you like see how much it'll cost? ")
        if total_price =="yes":
             print(sum(your_price))
        else:
             input("Press enter to exit")
    else:
        input("Press enter to exit")
else:
    print("Seems like you're not in the mood for shooping today!")