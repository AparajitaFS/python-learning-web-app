import functions
todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    if user_action:
        if user_action == 'add':
            todo = input("Enter a todo: ")
            todos.append(todo + "\n")
            functions.write_todos('todo.txt', todos)
        elif user_action == 'show':
            todos = functions.read_todos('todo.txt')
            for index, todoItem in enumerate(todos):
                newTodoItem = todoItem.strip('\n')
                print(f"{index + 1}. {newTodoItem.title()}")
        elif user_action == 'edit':
            todos = functions.read_todos('todo.txt')
            number = int(input("Enter todo number: "))-1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            functions.write_todos('todo.txt', todos)
        elif user_action == 'complete':
            todos = functions.read_todos('todo.txt')
            number = int(input("Enter todo number: "))-1
            completed_todo = todos[number].strip('\n')
            todos.pop(number)
            functions.write_todos('todo.txt', todos)
            print(f"{completed_todo} is completed")
        elif user_action == 'exit':
            print("Bye")
            exit()
        else:
            print("Please enter valid command!")