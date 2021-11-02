nested_dict = { 'soap': {'lux': 40, 'dove': 50, 'lifbouy': 45, 'dettol': 30},
                'oil': {'nihar': 60, 'jasmine': 40, 'parachute': 70, 'bajaj': 50},
                'shampoo': {'sunslik': 180,'clinic plus': 120, 'pantene': 150, 'dove': 250}}
my_cart = []
my_quantity = []
my_total= []
sum_total = 0
ask_name = input("Hi! Welcome to Megastore,Please enter your name: ")
cap_name = ask_name.capitalize()
while True:
    print("Hi {}, Mystore can help you with the following items: ".format(cap_name))
    for item in nested_dict:
        print(item)
    ask_user_category = input("Please select the category: ").lower()
    if ask_user_category in nested_dict:
        print("Hi we have the following brand with price for %s: {}".format(nested_dict[ask_user_category]) %ask_user_category)
        ask_brand = input("please select a brand you want: ").lower()
        if ask_brand in nested_dict[ask_user_category]:
            try:
                ask_quantity = float(input("Enter your quantity for {}: " .format(ask_brand)))
                add_quantity = nested_dict[ask_user_category][ask_brand]*ask_quantity
                print("The price of the item you have selected is {} for %d quantity".format(add_quantity) %ask_quantity)
                my_cart.append(ask_brand)
                my_quantity.append(ask_quantity)
                my_total.append(add_quantity)
                print("You have the following item in your cart: \nBrand Name: {} Quantity: {} Price: {}".format(my_cart,my_quantity,my_total))
            except:
                print("Please enter a valid quantity.")
            cont_shopping = input("write Yes to continue or write anything to exit(): ").lower()
            if cont_shopping == "yes":
                continue
            else:
                print("Final cart items:\n Items:{}\n Quantity:{}\n Price:{}\n".format(my_cart,my_quantity,my_total) )
                total_amount = sum(my_total)
                print("Grand Toatal= {}".format(total_amount))
                break
        else:
            print("This Item is not there in Mystore.")
    else:
        print("Sorry we donot have this product.")
        continue