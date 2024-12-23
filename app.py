import streamlit as st
import info

# Diccionario básico de usuarios y contraseñas

# Estado de sesión para gestionar si el usuario está logueado
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""

# Función de autenticación
def authenticate(username, password):
    if username in info.users and info.users[username] == password:
        return True
    return False

# Pantalla de login
def login_screen():
    st.title("Inicio de Sesión")
    with st.form("login_form"):
        username = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        submit = st.form_submit_button("Iniciar Sesión")
        
        if submit:
            if authenticate(username, password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"Bienvenido, {username}!")
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

# Pantalla principal después del login
def main_screen():
    st.title("¡Bienvenido!")
    st.write(f"Estás logueado como: **{st.session_state['username']}**")
    if st.button("Cerrar Sesión"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.rerun()

# Lógica de flujo
if st.session_state["logged_in"]:
    main_screen()
else:
    login_screen()
