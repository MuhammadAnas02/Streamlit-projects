import streamlit as st
import random
import string

def generate_password(lenght, used_digit , use_special):
    characters = string.ascii_letters

    if used_digit:
        characters +=string.digits

    if use_special:
        characters +=string.punctuation

    return "".join(random.choice(characters) for _ in range(lenght))


st.title("Password generator")

length = st.slider("Select a lenght of the password" , max_value=32 , min_value=8 , value=12)

used_digit  = st.checkbox("Include the number")

use_special_character = st.checkbox("special character included")

if st.button("generate_password"):
    password = generate_password(length , used_digit ,use_special_character )
    st.write(f"Genetrated password :{password}")


st.write("Made by Muhammad Anas")