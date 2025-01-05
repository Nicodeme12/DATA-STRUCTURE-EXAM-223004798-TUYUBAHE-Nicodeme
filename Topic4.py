class OrderNode:
    def __init__(self, order_id, order_details):
        self.order_id = order_id
        self.order_details = order_details
        self.next = None

class CircularOrderList:
    def __init__(self, max_orders):
        self.max_orders = max_orders
        self.current_size = 0
        self.head = None
        self.tail = None

    def add_order(self, order_id, order_details):
        new_order = OrderNode(order_id, order_details)
        if self.current_size < self.max_orders:
            if not self.head:
                self.head = self.tail = new_order
                self.tail.next = self.head  # Point tail back to head to form a circle
            else:
                self.tail.next = new_order
                self.tail = new_order
                self.tail.next = self.head
            self.current_size += 1
            print(f"Order '{order_id}' has been added to the list.")
        else:
            print(f"Max orders reached. Overwriting order '{self.head.order_id}' with new order '{order_id}'.")
            new_order.next = self.head.next
            self.head = new_order
            self.tail.next = self.head

    def display_orders(self):
        if not self.head:
            print("No orders in the list.")
            return
        print("Current Orders in the Circular List:")
        current = self.head
        count = 0
        while count < self.current_size:
            print(f"Order ID: {current.order_id}, Details: {current.order_details}")
            current = current.next
            count += 1

# Usage/execution
print("=== Circular Linked List Example ===")
order_list = CircularOrderList(max_orders=3)

order_list.add_order("O001", "Order for Rwandan Cuisine Class")
order_list.add_order("O002", "Order for East African Dishes Class")
order_list.add_order("O003", "Order for West African Flavors Class")

order_list.display_orders()
order_list.add_order("O004", "Order for Vegetarian African Recipes Class")
order_list.display_orders()
