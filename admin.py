import streamlit as st

def show_admin():
    st.title("🛠 Admin Panel")

    menu = st.sidebar.radio("Admin Menu", [
        "Dashboard",
        "User Management",
        "Resource Management",
        "Reports",
        "Site Settings",
        "Logout"
    ])

    if menu == "Dashboard":
        st.subheader("📊 Dashboard")
        st.write("System metrics overview.")
    elif menu == "User Management":
        st.subheader("👥 User Management")
        st.write("Manage users here.")
    elif menu == "Resource Management":
        st.subheader("📁 Resource Management")
        st.write("Upload and manage files/resources.")
    elif menu == "Reports":
        st.subheader("📈 Reports")
        st.write("Generate and view reports.")
    elif menu == "Site Settings":
        st.subheader("⚙ Site Settings")
        st.write("Adjust your platform settings.")
    elif menu == "Logout":
        st.success("Logged out. Return to Home.")
        st.experimental_rerun()