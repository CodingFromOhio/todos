import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    if todo.strip() != '':
        todos.append(todo)
        functions.write_todos(todos_arg=todos)
    else:
        pass


st.title('My todo app')
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Write a todo', on_change=add_todo, key='new_todo')

# st.session_state
