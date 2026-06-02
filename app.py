  import streamlit as st
  st.title("Keterfoods Admin Portal")
  role = st.text_input("Enter 'admin' or 'user'")
  if role == "admin":
      password = st.text_input("Enter the password", type="password").lower()
      if password == "plazmazerora":
          st.success("Welcome master")
  elif role == "user":
      st.write("Welcome user")
