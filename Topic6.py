class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

class CookingClassTree:
    def __init__(self):
        self.root = None

    def set_root(self, name):
        self.root = TreeNode(name)
        print(f"Root category '{name}' created.")

    def add_category(self, parent_name, category_name):
        parent_node = self._find_node(self.root, parent_name)
        if parent_node:
            new_category = TreeNode(category_name)
            parent_node.children.append(new_category)
            print(f"Category '{category_name}' added under '{parent_name}'.")
        else:
            print(f"Parent category '{parent_name}' not found.")

    def add_course(self, category_name, course_name):
        category_node = self._find_node(self.root, category_name)
        if category_node:
            course_node = TreeNode(course_name)
            category_node.children.append(course_node)
            print(f"Course '{course_name}' added under category '{category_name}'.")
        else:
            print(f"Category '{category_name}' not found.")

    def _find_node(self, node, name):
        if not node:
            return None
        if node.name == name:
            return node
        for child in node.children:
            result = self._find_node(child, name)
            if result:
                return result
        return None

    def display(self):
        if not self.root:
            print("No categories available.")
            return
        print("Cooking Classes Hierarchy:")
        self._display_tree(self.root, 0)

    def _display_tree(self, node, level):
        print("  " * level + node.name)
        for child in node.children:
            self._display_tree(child, level + 1)

print("=== Cooking Class Hierarchy Example ===")
class_tree = CookingClassTree()

class_tree.set_root("Cooking Classes")
class_tree.add_category("Cooking Classes", "African Cuisine")
class_tree.add_category("Cooking Classes", "Asian Cuisine")
class_tree.add_category("African Cuisine", "Rwandan Cuisine")
class_tree.add_category("African Cuisine", "East African Dishes")
class_tree.add_category("Asian Cuisine", "Chinese Cuisine")

class_tree.add_course("Rwandan Cuisine", "Making Isombe")
class_tree.add_course("East African Dishes", "Preparing Ugali and Sukuma Wiki")
class_tree.add_course("Chinese Cuisine", "Preparing Dim Sum")

class_tree.display()
