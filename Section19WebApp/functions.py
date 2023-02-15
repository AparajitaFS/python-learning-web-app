filepath = 'todo.txt'


def read_todos(FILEPATH=filepath):
    with open(filepath, 'r') as file:
        todosList = file.readlines()
    return todosList


def write_todos(todos, FILEPATH=filepath):
    with open(filepath, 'w') as file:
        file.writelines(todos)
