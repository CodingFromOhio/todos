FILEPATH = 'todos.txt'


def get_todos(file_path=FILEPATH):
    """ Read a text file and
    Returns the list of the todo items
    """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """Writes todos to a text file"""
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
