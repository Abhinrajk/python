

#4 OnlineShoppingCartSystem




cart = {}

def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    
    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}
    
    print(f"{name} added to cart.\n")

def remove_item():
    name = input("Enter item name to remove: ")
    
    if name in cart:
        del cart[name]
        print(f"{name} removed from cart.\n")
    else:
        print("Item not found in cart.\n")

def calculate_total():
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    return total

def apply_discount(total):
    discount = 0
    if total >= 1000:
        discount = total * 0.10   # 10% discount
    return total - discount

def display_cart():
    if not cart:
        print("Cart is empty.\n")
        return
    
    print("\nItems in Cart:")
    for name, item in cart.items():
        print(f"{name} - Price: {item['price']} Quantity: {item['quantity']}")
    
    total = calculate_total()
    final_amount = apply_discount(total)
    
    print(f"\nTotal Bill: ₹{total}")
    print(f"Final Amount after Discount: ₹{final_amount}\n")


while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart & Bill")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_cart()
    elif choice == "4":
        print("Thank you for shopping! 🛍️")
        break
    else:
        print("Invalid choice. Try again.\n")
