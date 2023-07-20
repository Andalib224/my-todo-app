FILEPATH = "todos.txt"


def get_todos(filename=FILEPATH):
    """Read to-do items list from a text file and return todo list."""

    with open(filename, 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(todos, filename=FILEPATH):
    """Write the todo item list to a text file"""

    with open(filename, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("I am from function module")
    print("This is a function ")
