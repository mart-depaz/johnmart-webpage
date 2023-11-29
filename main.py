from PIL import Image
import streamlit as st
import hobbies
import family
import friends

st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

img_contact_form = Image.open("images/profile-pic (1).png")

with st.container():
    st.subheader("Hi:wave: Welcome to my webpage")
    st.title("I am John Mart E. De Paz a student of SNSU")
    st.write("Studying Bachelor of Science in Computer Engineering")
   
with st.container():
    st.write("---")
    st.title("Who is John Mart")
    left_column, right_column = st.columns(2)
    with left_column:
        left_column_one, right_column_one = st.columns(2)
        with left_column_one:
            st.write("##")
            st.image(img_contact_form)
        with right_column_one:
            st.write("##")
            st.write("##")
            st.write("I'm a person who's quietly strong and often seen as shy. School is important to me, and I'm proud to be a good student. I can be reserved sometimes, but I switch between being someone who likes alone time and someone who enjoys being around others. I want a calm life, and in the middle of it all, I love having a cup of coffee it's like a friend. I have big dreams and am working hard to reach my goals, creating a path that combines my quiet thoughts and outgoing dreams.")
    st.write("If you want to friend me on Facebook Just Click Here [Learn More >](https://www.facebook.com/jhonmart.depaz)")     
    st.write("---")
    st.header("If you want to know more about me just select the options below:")
    myself = st.radio("",("My Hobbies", "My Family", "My Friends"))
    button1 = st.button("Submit")
    st.write("---")
    if button1:
        if myself == "My Hobbies":
            hobbies.app()
        elif myself == "My Family":
            family.app()
        elif myself == "My Friends":
            friends.app()
            
with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("☎️ Contact")
            st.write("You can message and contact me if you want")
            st.write("##")
            
            contact_form = """
                <form action="https://formsubmit.co/johnmartdepaz77@gmail.com" method="POST">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
                </form>
            """
            
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()
        
            
