FILEPATH = "todos.txt"


def get_todos(filepath_local=FILEPATH):
    """ Read a text file and return a list of
    to-do items.
    """
    # with context manager
    with open(filepath_local, 'r') as file_local:
        return file_local.readlines()


def write_todos(todos_local, filepath_local=FILEPATH):
    """ Write the to-do items list to a text file"""
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_local)


# only execute this code if this script is executed directly
if __name__ == "__main__":
    print("Hello")
    print(get_todos())