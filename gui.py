import streamlit as st

st.title("Hi 36 cedar")
st.subheader("This is todo app")
st.subheader("Double click on the check box to delete the completed todo")

add_todo = st.text_input("enter something")
print(add_todo)


def get_todos():
    with open("todos.txt", 'r') as file:
        todos = file.readlines()
        return todos


x = get_todos()

if add_todo.strip():  # Check if the input is not empty after removing leading/trailing spaces
    x.append(f"{add_todo}\n")


def write_todos():
    with open("todos.txt", 'w') as file:
        file.writelines(x)


write_todos()
x = get_todos()
for i, j in enumerate(get_todos()):
    check = st.checkbox(j, key=i)
    if check:
        x.pop(i)
        write_todos()

