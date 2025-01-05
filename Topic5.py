class AVLNode:
    def __init__(self, category_name):
        self.category_name = category_name
        self.courses = []
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, category_name):
        if not root:
            print(f"Category '{category_name}' has been added.")
            return AVLNode(category_name)
        elif category_name < root.category_name:
            root.left = self.insert(root.left, category_name)
        elif category_name > root.category_name:
            root.right = self.insert(root.right, category_name)
        else:
            print(f"Category '{category_name}' already exists. No duplicates allowed.")
            return root

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        balance = self._get_balance(root)

        if balance > 1 and category_name < root.left.category_name:
            return self._rotate_right(root)
        if balance < -1 and category_name > root.right.category_name:
            return self._rotate_left(root)
        if balance > 1 and category_name > root.left.category_name:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)
        if balance < -1 and category_name < root.right.category_name:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def add_course(self, category_name, course_name):
        node = self._find_category(self.root, category_name)
        if node:
            node.courses.append(course_name)
            print(f"Course '{course_name}' added to category '{category_name}'.")
        else:
            print(f"Error: Category '{category_name}' not found. Unable to add course '{course_name}'.")

    def _find_category(self, root, category_name):
        if not root:
            return None
        if root.category_name == category_name:
            return root
        elif category_name < root.category_name:
            return self._find_category(root.left, category_name)
        else:
            return self._find_category(root.right, category_name)

    def display(self):
        if not self.root:
            print("No categories available.")
            return
        print("Available Categories and Their Courses:")
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, root):
        if root:
            self._in_order_traversal(root.left)
            print(f"Category: {root.category_name}")
            if root.courses:
                for course in root.courses:
                    print(f"  - {course}")
            else:
                print("  No courses added to this category yet.")
            self._in_order_traversal(root.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

print("=== AVL Tree Example ===")
avl_tree = AVLTree()
avl_tree.root = avl_tree.insert(avl_tree.root, "Rwandan Cuisine")
avl_tree.root = avl_tree.insert(avl_tree.root, "East African Dishes")
avl_tree.root = avl_tree.insert(avl_tree.root, "West African Flavors")
avl_tree.root = avl_tree.insert(avl_tree.root, "Vegetarian African Delicacies")
avl_tree.add_course("Rwandan Cuisine", "Making Isombe")
avl_tree.add_course("East African Dishes", "Preparing Ugali and Sukuma Wiki")
avl_tree.add_course("West African Flavors", "Exploring Jollof Rice")
avl_tree.add_course("Vegetarian African Delicacies", "Cooking Plant-Based Matoke")
avl_tree.display()
