class CoffeeShop:
    def __init__(self):
        self.menu = {
            "C1": ("Espresso", 2.50),
            "C2": ("Latte", 3.00),
            "C3": ("Cappuccino", 3.50),
            "C4": ("Americano", 2.75),
            "C5": ("Mocha", 4.00)
        }
        self.cart = []

    def display_menu(self):
        
        print("\n---Coffee Menu---")
        
        for code, (item, price) in self.menu.items():
        
            print(f"{code}: {item} - ${price:.2f}")

    def add_to_cart(self, code, quantity):
        
        if code in self.menu:
        
            item, price = self.menu[code]
        
            self.cart.append({"item": item, "price": price, "quantity": quantity})
        
            print(f"Added {quantity} x {item} to your cart.")
        
        else:
        
            print("Invalid code. Please try again.")

    def view_cart(self):
        
        if not self.cart:
        
            print("\nYour cart is empty.")
        
        else:
        
            print("\n---Your Cart---")
        
            total = 0
        
            for entry in self.cart:
        
                item_total = entry["price"] * entry["quantity"]
        
                total += item_total
        
                print(f"{entry['quantity']} x {entry['item']} - ${item_total:.2f}")
        
            print(f"Total: ${total:.2f}")


    def checkout(self):

        if not self.cart:

            print("\nYour cart is empty. Add items before checking out.")

        else:

            self.view_cart()

            print("Thank you for your order!")

            self.cart = []

class CoffeeOrderingApp:

    def __init__(self):

        self.shop = CoffeeShop()

    def run(self):

        while True:

            print("\n---Coffee Ordering App---")

            print("1. View Menu")

            print("2. Place Order")

            print("3. View Cart")

            print("4. Checkout")

            print("5. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":

                self.shop.display_menu()

            elif choice == "2":

                self.place_order()

            elif choice == "3":

                self.shop.view_cart()

            elif choice == "4":

                self.shop.checkout()

            elif choice == "5":

                print("Thank you for visiting the Coffee Shop! Goodbye!")

                break

            else:

                print("Invalid choice. Please try again.")

    def place_order(self):

        while True:

            self.shop.display_menu()

            code = input("Enter the code of the coffee you want to order (or type 'done' to finish): ").strip()

            if code.lower() == "done":

                break

            elif code in self.shop.menu:

                quantity = input(f"Enter the quantity for {self.shop.menu[code][0]}: ").strip()

                if quantity.isdigit() and int(quantity) > 0:

                    self.shop.add_to_cart(code, int(quantity))

                else:

                    print("Invalid quantity. Please enter a positive number.")

            else:

                print("Invalid code. Please try again.")

# Main

if __name__ == "__main__":

    app = CoffeeOrderingApp()

    app.run()
