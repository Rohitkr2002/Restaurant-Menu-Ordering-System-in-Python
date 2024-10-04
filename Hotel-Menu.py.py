#Define the menu of Restaurent
menu = {
    'Pizza':40,
    'Pasta':50,
    'Salads':30,
    'Burgers':60,
    'Sandwiches':70,
    'Fries':20,
    'Water':20,
    'Soda':30,
    'Juice':40,
    'Coffee': 80,
}

# Greet

print("Welcome to our Restaurant!")
print("Here is our menu:")
print("1. Pizza - Rs40\n2. Pasta - Rs50\n3. Salads - Rs30\n4. Burgers - Rs60\n5. Sandwiches - Rs60\n6. Fries - Rs20\n7. Water - Rs20\n8. Soda - Rs30\n9. Juice - Rs40\n10. Coffee - Rs80") 

order_total = 0

item_1 = input("Enter the name of item you want to oder = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item(Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of secomd item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Odered item {item_2} is not avaialable yet!")

print(f"The total amount of item to pay is {order_total}")