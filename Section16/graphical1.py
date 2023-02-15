import PySimpleGUI as sg
import functions

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(),
                      key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
layout = [[label], [input_box, add_button], [list_box, edit_button]]
window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'][0])
    if event:
        if "Add" in event:
            todos = functions.read_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos, 'todo.txt')
            window['todos'].update(values=todos)
        if "Edit" in event:
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.read_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        if "todos" in event:
            window["todo"].update(value=values['todos'][0])
        if sg.WINDOW_CLOSED:
            exit()

window.close()