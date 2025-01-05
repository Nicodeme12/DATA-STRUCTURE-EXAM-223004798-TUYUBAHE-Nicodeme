class CookingClassItem:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __str__(self):
        return f"{self.name} (Priority: {self.priority})"

class CookingClassPlatform:
    def __init__(self):
        self.items = []

    def add_item(self, name, priority):
        self.items.append(CookingClassItem(name, priority))
        print(f"Item '{name}' with priority {priority} added.")

    def bubble_sort(self):
        n = len(self.items)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if self.items[j].priority > self.items[j + 1].priority:
                    self.items[j], self.items[j + 1] = self.items[j + 1], self.items[j]
                    swapped = True
            if not swapped:
                break
        print("Items sorted by priority.")

    def display_items(self):
        if not self.items:
            print("No items available.")
            return
        print("Items:")
        for item in self.items:
            print(item)

print("=== Bubble Sort Example ===")
platform = CookingClassPlatform()

platform.add_item("Making Isombe", 3)
platform.add_item("Preparing Ugali and Sukuma Wiki", 1)
platform.add_item("Exploring Jollof Rice", 4)
platform.add_item("Cooking Plant-Based Matoke", 2)

print("\nBefore Sorting:")
platform.display_items()

platform.bubble_sort()

print("\nAfter Sorting:")
platform.display_items()
