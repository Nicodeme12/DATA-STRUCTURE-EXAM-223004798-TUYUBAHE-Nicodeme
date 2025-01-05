class CategoryNode:
    def __init__(self, category_name):
        self.category_name = category_name
        self.courses = []
        self.left = None
        self.right = None

class CookingClassPlatform:
    def __init__(self):
        self.root = None

    def add_category(self, category_name):
        if not self.root:
            self.root = CategoryNode(category_name)
            print(f"Category '{category_name}' has been added as the root.")
        else:
            self._add_category_recursive(self.root, category_name)
            print(f"Category '{category_name}' has been successfully added.")

    def _add_category_recursive(self, current_node, category_name):
        if category_name < current_node.category_name:
            if current_node.left is None:
                current_node.left = CategoryNode(category_name)
            else:
                self._add_category_recursive(current_node.left, category_name)
        elif category_name > current_node.category_name:
            if current_node.right is None:
                current_node.right = CategoryNode(category_name)
            else:
                self._add_category_recursive(current_node.right, category_name)

    def add_course(self, category_name, course_name):
        category_node = self._find_category(self.root, category_name)
        if category_node:
            category_node.courses.append(course_name)
            print(f"Course '{course_name}' has been added to the category '{category_name}'.")
        else:
            print(f"Error: Category '{category_name}' does not exist. Unable to add course '{course_name}'.")

    def _find_category(self, current_node, category_name):
        if not current_node:
            return None
        if current_node.category_name == category_name:
            return current_node
        elif category_name < current_node.category_name:
            return self._find_category(current_node.left, category_name)
        else:
            return self._find_category(current_node.right, category_name)

    def display_all_categories_and_courses(self):
        if not self.root:
            print("No categories are available yet.")
            return
        print("Available Categories and Their Courses:")
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, current_node):
        if current_node:
            self._in_order_traversal(current_node.left)
            print(f"Category: {current_node.category_name}")
            if current_node.courses:
                for course in current_node.courses:
                    print(f"  - {course}")
            else:
                print("  No courses added to this category yet.")
            self._in_order_traversal(current_node.right)

# execution
platform = CookingClassPlatform()

platform.add_category("Rwandan Cuisine")
platform.add_category("East African Dishes")
platform.add_category("West African Flavors")
platform.add_category("Vegetarian African Delicacies")

platform.add_course("Rwandan Cuisine", "Making Isombe")
platform.add_course("East African Dishes", "Preparing Ugali and Sukuma Wiki")
platform.add_course("West African Flavors", "Exploring Jollof Rice")
platform.add_course("Vegetarian African Delicacies", "Cooking Plant-Based Matoke")

platform.display_all_categories_and_courses()
