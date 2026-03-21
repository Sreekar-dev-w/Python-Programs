# Without using enum, create a simple shop cart system that allows users to add items, remove items, and view the cart. The system should continue to run until the user chooses to exit.

base=[]
print("Welcome to the shop cart system!")
print("1.Add item\n2.Remove item\n3.View cart\n4.Exit")
while True:
    choice=int(input("Enter your choice: "))
    if choice==1:
        item=input("Enter the item you want to add: ")
        base.append(item)
        print(f"{item} has been added to the cart.")
    elif choice==2:
        item=input("Enter the item you want to remove: ")
        if item in base:
            base.remove(item)
            print(f"{item} has been removed from the cart.")
        else:
            print(f"{item} is not in the cart.")
    elif choice==3:
        if base:
            print("Items in your cart:")
            for i, item in enumerate(base, 1):
                print(f"{i}. {item}")
        else:
            print("Your cart is empty.")
    elif choice==4:
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please try again.")
    
