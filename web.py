import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("this is my todo app")
st.write("This app to increase your ass weight")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f'checkbox_{index}')
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter A ToDo", placeholder= "Add new todo...",
              on_change=add_todo, key='new_todo')


