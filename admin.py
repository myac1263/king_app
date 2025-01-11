import streamlit as st
from login import create_user

USER_ROLES = {}  # Simulating user roles

def display_admin_panel():

    st.subheader("Admin Panel: Create new users and manage roles")
    new_user = st.text_input("New Username", key="new_user")
    new_password = st.text_input("New Password", type="password", key="new_password")
    
    role_options = ["Admin", "Moderator", "User"]
    selected_role = st.selectbox("Select Role", role_options)

    if st.button("Create User"):
        if new_user and new_password:
            USER_ROLES[new_user] = {"password": new_password, "role": selected_role}
            create_user(new_user, new_password)
            st.success(f"User {new_user} created with role {selected_role}!")
        else:
            st.error("Username and password cannot be empty.")

    # Display and manage users
    st.write("Existing Users and Roles:")
    for username, data in USER_ROLES.items():
        st.write(f"{username}: {data['role']}")

    # Update user role
    update_user = st.selectbox("Select User to Update", list(USER_ROLES.keys()))
    new_role = st.selectbox("New Role", role_options)
    
    if st.button("Update Role"):
        if update_user:
            USER_ROLES[update_user]["role"] = new_role
            st.success(f"User {update_user}'s role updated to {new_role}.")
