import streamlit as st
from home import show_home
from login import show_login
from signup import show_signup
from admin import show_admin

st.set_page_config(page_title="My Web App", layout="centered")

# Sidebar Menu
menu = st.sidebar.selectbox("Navigate", ["Home", "Login", "Sign Up", "Admin"])

# Page Routing
if menu == "Home":
    show_home()
elif menu == "Login":
    show_login()
elif menu == "Sign Up":
    show_signup()
elif menu == "Admin":
    show_admin()