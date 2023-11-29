from PIL import Image
import streamlit as st

def app ():
    
    img_contact_form = Image.open("images/images.jpg")
    img_contact_form1 = Image.open("images/download.jpg")
    img_contact_form2 = Image.open("images/download (1).jpg")
    img_contact_form3 = Image.open("images/download (2).jpg")
    img_contact_form4 = Image.open("images/download (3).jpg")
    
   
    st.title("My Hobbies")
    st.write("##")
    
    st.write("---")
    with st.container ():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.header("PLAYING MY FAVORITE INSTRUMENT")
            st.write("The guitar is my musical companion, and strumming its strings feels like a conversation with an old friend. It adds a unique flavor to the melodies I create, allowing me to explore various genres and infuse my own style into each chord.")
    st.write("---")
    st.write("##")
    with st.container ():
        left_column, right_column = st.columns(2)
        image_column, text_column = st.columns((1, 2)) 
        with image_column:
            with left_column:
                st.header("Listening to Music")
                st.write("##")
                st.write("Music is my escape into a world where every note carries its own emotion. Whether it's the rhythmic beats of drums or the gentle hum of a piano, creating music is my way of translating feelings into a language that everyone can understand, even without words.")
            with right_column:
                st.write("##")
                st.image(img_contact_form1)
    st.write("---")
    st.write("##")
    with st.container ():
        left_column, right_column = st.columns(2)
        image_column, text_column = st.columns((1, 2))
        with image_column:
            with left_column:
                st.write("##")
                st.image(img_contact_form2)
            with right_column:
                st.write("##")
                st.header("SINGING")
                st.write("Singing is like painting with my voice. It's a way to express emotions, tell stories, and connect with others. From upbeat tunes to soulful ballads, singing allows me to share a piece of myself through the melody and lyrics.")
    st.write("---")
    st.write("##")
    with st.container ():
        left_column, right_column = st.columns(2)
        image_column, text_column = st.columns((1, 2))
        with image_column:
            with left_column:
                st.write("##")
                st.header("Solving MATH Problem")
                st.write("Solving math problems is like solving puzzles for fun. It's a challenge that stimulates my mind and satisfies my curiosity. Finding solutions feels like discovering hidden paths, and each problem cracked is a small victory that fuels my love for unraveling the mysteries of numbers.")
            with right_column:
                st.write("##")
                st.image(img_contact_form3)
    st.write("---")
    st.write("##")
    with st.container ():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.write("##")
            st.image(img_contact_form4)
        with text_column:
            st.write("##")
            st.header("CODING") 
            st.write("I enjoy Python because it's beginner-friendly with its straightforward code. It allows me to tackle various projects, from creating websites to analyzing data. The satisfaction of solving problems and building functional apps is fulfilling and fuels my love for programming. Moreover, staying engaged by learning new things as technology evolves adds excitement to my programming journey.") 
    st.write("---")