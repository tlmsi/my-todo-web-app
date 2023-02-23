def get_todos(filepath="todos.txt"):
    """ Read the text file and return the to-do's list
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-dos item list into text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())