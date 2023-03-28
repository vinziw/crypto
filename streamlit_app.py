import streamlit as st
from hashlib import sha256


def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

st.title("Leni's & Fifi's Crypto Tools!")

st.header('Caesar Cipher')

input = st.text_input('Input')
rot = st.number_input('Rotations', step =1)

#st.write(test)

st.caption('Caesar cipher output:')
st.write(encrypt_text(input,rot))
st.caption('SHA-256 output:')
st.write(sha256(input.encode('utf-8')).hexdigest())

st.header('Guess the hasehd word (SHA-256)')
col1,col2 = st.columns(2)
with col1:
    guess1 = st.text_input('Current topic')
    st.caption('Hashed Input:')

    st.write(sha256(guess1.encode('utf-8')).hexdigest())
    st.caption('Searched word hashed with SHA-256:')
    st.write(sha256('crypto'.encode('utf-8')).hexdigest())
    if guess1 == "crypto":

        st.markdown(
            """
        <style>
            div[data-testid="column"]:nth-of-type(1)
            {
                color: green;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
with col2:
    guess2 = st.text_input('Crypto currency')
    st.caption('Hashed Input:')
    st.write(sha256(guess2.encode('utf-8')).hexdigest())
    st.caption('Searched word hashed with SHA-256:')
    st.write(sha256('bitcoin'.encode('utf-8')).hexdigest())

    if guess2 == "bitcoin":
        st.markdown(
            """
        <style>
            div[data-testid="column"]:nth-of-type(2)
            {
                color: green;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
