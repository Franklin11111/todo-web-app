import streamlit as st

from modules import functions

todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.session_state["new_todo"] = ""
st.text_input("Add todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
