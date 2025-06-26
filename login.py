import streamlit as st

def show_login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome back, {username}!")