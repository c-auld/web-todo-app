import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    print("Adding todo")
    todo = st.session_state["new_todo"]
    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)

def complete_todos():
    modified_todos = todos.copy()
    for todo in todos:
        checked_todo = st.session_state[todo]
        if checked_todo:
            modified_todos.remove(todo)

    functions.write_todos(modified_todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This is an app to keep track of your life!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)


st.button(label="Complete", on_click=complete_todos)

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")
st.session_state