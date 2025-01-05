class BinaryTreeNode:
    def __init__(self, category):
        self.category = category
        self.courses = []
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, category):
        if not self.root:
            self.root = BinaryTreeNode(category)
            print(f"Category '{category}' added as the root category.")
        else:
            self._insert_recursive(self.root, category)
            print(f"Category '{category}' added successfully.")

    def _insert_recursive(self, node, category):
        if category < node.category:
            if node.left is None:
                node.left = BinaryTreeNode(category)
            else:
                self._insert_recursive(node.left, category)
        elif category > node.category:
            if node.right is None:
                node.right = BinaryTreeNode(category)
            else:
                self._insert_recursive(node.right, category)

    def add_course_to_category(self, category, course):
        node = self._find_category(self.root, category)
        if node:
            node.courses.append(course)
            print(f"Course '{course}' added to category '{category}'.")
        else:
            print(f"Category '{category}' not found. Course '{course}' not added.")

    def _find_category(self, node, category):
        if not node:
            return None
        if node.category == category:
            return node
        elif category < node.category:
            return self._find_category(node.left, category)
        else:
            return self._find_category(node.right, category)

    def display_categories_and_courses(self):
        categories = []
        self._in_order_traversal(self.root, categories)
        return categories

    def _in_order_traversal(self, node, categories):
        if node:
            self._in_order_traversal(node.left, categories)
            categories.append((node.category, node.courses))
            self._in_order_traversal(node.right, categories)

class DoublyLinkedListNode:
    def __init__(self, course):
        self.course = course
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_course(self, course):
        new_node = DoublyLinkedListNode(course)
        if not self.head:
            self.head = self.tail = new_node
            print(f"Course '{course}' added as the first completed course.")
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            print(f"Course '{course}' added to the user progress.")

    def display_progress(self):
        courses = []
        current = self.head
        while current:
            courses.append(current.course)
            current = current.next
        return courses

print("Binary Tree:")
course_tree = BinaryTree()
course_tree.insert("Rwandan Cuisine")
course_tree.insert("East African Dishes")
course_tree.insert("West African Spices")
course_tree.insert("Vegetarian African Recipes")

course_tree.add_course_to_category("Rwandan Cuisine", "Making Isombe")
course_tree.add_course_to_category("East African Dishes", "Preparing Ugali and Sukuma Wiki")
course_tree.add_course_to_category("West African Spices", "Exploring Jollof Rice Recipes")
course_tree.add_course_to_category("Vegetarian African Recipes", "Cooking Plant-Based Matoke")

print("Course Categories and Courses:")
for category, courses in course_tree.display_categories_and_courses():
    print(f"Category: {category}")
    for course in courses:
        print(f"  - {course}")

print("\nDoublyLinkedList :")
user_progress = DoublyLinkedList()
user_progress.add_course("Making Isombe")
user_progress.add_course("Preparing Ugali and Sukuma Wiki")
user_progress.add_course("Exploring Jollof Rice Recipes")

print("User Progress:")
for course in user_progress.display_progress():
    print(f"  - {course}")
