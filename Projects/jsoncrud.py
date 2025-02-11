import json

class SwiggyOrderSystem:
    def __init__(self, json_file):
        self.json_file = json_file
        self.load_data()

    def load_data(self):
        try:
            with open(self.json_file, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []
        except json.JSONDecodeError:
            print("Error: JSON decode error. Starting with an empty list.")
            self.data = []

    def save_data(self):
        try:
            with open(self.json_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError:
            print("Error: Unable to save data to file.")

    def create_order(self, order):
        self.data.append(order)
        self.save_data()

    def read_order(self, order_id):
        for order in self.data:
            if order['id'] == order_id:
                return order
        return None

    def update_order(self, order_id, updated_order):
        for index, order in enumerate(self.data):
            if order['id'] == order_id:
                self.data[index] = updated_order
                self.save_data()
                return True
        return False

    def delete_order(self, order_id):
        for index, order in enumerate(self.data):
            if order['id'] == order_id:
                del self.data[index]
                self.save_data()
                return True
        return False

if __name__ == "__main__":
    system = SwiggyOrderSystem('orders.json')
    
    while True:
        print("\n1. Create Order\n2. Read Order\n3. Update Order\n4. Delete Order\n5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                order = {
                    'id': int(input("Enter order ID: ")),
                    'customer_name': input("Enter customer name: "),
                    'items': input("Enter items (comma separated): ").split(','),
                    'total_price': float(input("Enter total price: "))
                }
                system.create_order(order)
                print("Order created successfully.")
            
            elif choice == '2':
                order_id = int(input("Enter order ID to read: "))
                order = system.read_order(order_id)
                if order:
                    print("Order details:", order)
                else:
                    print("Order not found.")
            
            elif choice == '3':
                order_id = int(input("Enter order ID to update: "))
                updated_order = {
                    'id': order_id,
                    'customer_name': input("Enter new customer name: "),
                    'items': input("Enter new items (comma separated): ").split(','),
                    'total_price': float(input("Enter new total price: "))
                }
                if system.update_order(order_id, updated_order):
                    print("Order updated successfully.")
                else:
                    print("Order not found.")
            
            elif choice == '4':
                order_id = int(input("Enter order ID to delete: "))
                if system.delete_order(order_id):
                    print("Order deleted successfully.")
                else:
                    print("Order not found.")
            
            elif choice == '5':
                break
            
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values for ID and price.")
