
class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root is None:
            print("Error: Add a team lead first.")
            return False

        side = side.lower()

        if side not in ("left", "right"):
            print("Error: Please choose left or right.")
            return False

        if current_node is None:
            current_node = self.root

        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    return True
                else:
                    print("Error: The left side is already taken.")
                    return False

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    return True
                else:
                    print("Error: The right side is already taken.")
                    return False

        if current_node.left is not None:
            if self.insert(manager_name, employee_name, side, current_node.left):
                return True

        if current_node.right is not None:
            if self.insert(manager_name, employee_name, side, current_node.right):
                return True

        if current_node == self.root:
            print("Error: Manager not found.")

        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        if node is None:
            print("The team directory is empty.")
            return

        print("  " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


def company_directory():
    company = TeamTree()

    while True:
        print("\nTeam Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if company.root is not None:
                print("Error: A team lead already exists.")
            else:
                name = input("Enter team lead's name: ").strip()

                if name:
                    company.root = EmployeeNode(name)
                    print(f"{name} added as the team lead.")
                else:
                    print("Error: Name cannot be empty.")

        elif choice == "2":
            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should this employee be on the LEFT or RIGHT? "
            ).strip().lower()

            if not manager or not employee:
                print("Error: Names cannot be empty.")
            elif company.insert(manager, employee, side):
                print(f"{employee} added to the {side.upper()} of {manager}.")

        elif choice == "3":
            print("\nCurrent Team Structure:")
            company.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    company_directory()
