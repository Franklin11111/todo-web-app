def get_todos(filepath="todos.txt"):
    """ Reads the text file and returns the content as list with each value being
    equal to each line read from the text file."""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local
#print(help(get_todos))

def write_todos(todo_list, filepath="todos.txt"):
    """Creates a new text file and adds the content received from updated list"""
    with open(filepath, "w") as file:
        file.writelines(todo_list)

print(__name__)
if __name__ == "__main__":
    print("Hello")
