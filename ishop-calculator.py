items = []
prices = []

print("\n***** Welcome to iShop calculator *****")
numbers = int(input("\nHow many items are there in your basket today? "))

if numbers > 0:
    print("\nLets get to counting them ....")

    for i in range(1,numbers + 1):
 
            name = input(f"Please tell me the name of the item number {i}: ").lower()
            items.append(name)

            price = float(input(f"What is the price of {name} \n$"))
            prices.append(price)

    choice = input("Would you like to see your entire basket items? ").lower()
    if choice == "yes":
        print(f"{items}")

    choice = input(f"Would you like to see how much it'll coast? ")
    if choice == "yes":
        print(f"\nBuying these items will cost:\n${sum(prices)}")
        print("\nThanks for using this application!")
    else:
        print("\nThanks for using this application!")

else:
     print("Seems like you are not in the mood for shopping today")
