from PIL import Image
import streamlit as st

def app ():
    
    img_contact_form = Image.open("images/400559122_1037120160762243_5761796664244611032_n.jpg")
    
    st.title("My FRIENDS")
    st.write("##")
    
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.header("My Buddies")
            st.write("As a student, my friends are like the sunshine in my school days. They bring laughter into our world, turning even the gloomiest moments into something bright and cheerful. We stick together through thick and thin, always ready to lend a hand when one of us is stuck with a tricky assignment. They are my go-to people for a good laugh or a comforting chat when things get tough. In this journey of learning, they are not just classmates; they are my partners in the adventure called school, making each day a bit more enjoyable and a lot less stressful.")
        st.write("---")