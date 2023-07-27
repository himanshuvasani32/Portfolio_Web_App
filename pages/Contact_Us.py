import streamlit as st

st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Enter your email:')
    message = st.text_area('Enter your message:')
    button = st.form_submit_button('Submit')
