from PIL import Image
import streamlit as st

def app ():
    
    img_contact_form = Image.open("images/65762255_2460323594197200_7269779477637365760_n.jpg")
    img_contact_form1 = Image.open("images/382993825_1736609776777476_7664839625155856893_n.jpg")
    img_contact_form2 = Image.open("images/192848898_124006639937310_7683433302382916423_n.jpg")
    
    
    st.title("My FAMILY")
    st.write("##")
    st.write("---")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_form)
        with text_column:
            st.header("My Mother and Father")
            st.write("Mama is the heart of our home. She's the one who cooks delicious meals, tells bedtime stories, and gives the warmest hugs. Her love is like a cozy blanket that makes everything feel just right. Papa is my superhero. He fixes things, teaches me cool stuff, and is always there when I need help. His laughter is the soundtrack of our home, and his advice is like a compass guiding me through life's adventures. Together, Mama and Papa make our family a wonderful place to be.")
    st.write("---")
    st.write("##")
    with st.container():
        left_column, right_column = st.columns(2)
        image_column, text_column = st.columns((1, 2))   
        with image_column:
            with left_column:
                st.header("My Sister and Nephew")
                st.write("##")
                st.write("My sister is like a built-in friend. She's someone I can share secrets with, laugh together, and rely on when things get tough. She knows me really well because we've been through a lot together. She's not just family; she's a big part of my life. My sister's son is my nephew, and he's like a little bundle of joy in our family. He's the child of my sister, so we're all connected. I get to watch him grow, play with him, and be a part of his adventures. It's amazing to see bits of both my sister and me in this little guy.")
        with text_column:
            with right_column:
                st.image(img_contact_form1)
    st.write("---")
    st.write("##")
    with st.container():
        image_column, text_column = st.columns((1, 2))   
        with image_column:
            st.image(img_contact_form2)
        with text_column:
            st.header("My Brother")
            st.write("##")
            st.write("My big brother is like my guide in this big adventure called life. He's the one who helps me when things get tricky, shares funny stories, and sometimes even shares his snacks. He's a bit like a superhero, watching out for me and teaching me cool stuff along the way. I feel safe and happy when he's around.")
    st.write("---")   