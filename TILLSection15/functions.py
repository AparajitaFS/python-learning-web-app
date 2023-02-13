
def read_todos(filepath):
    with open(filepath, 'r') as file:
        todosList = file.readlines()
    return todosList
def write_todos(filepath, todos):
    with open(filepath, 'w') as file:
        file.writelines(todos)



