import streamlit as st
st.set_page_config(layout="wide")

st.title('Elizabeth Sarah McNaughton')

container = st.container()

(container.write('my description of her'))

Memories, Inside_Jokes = st.tabs(["Memories", "Inside Jokes"])

with Memories:

    col1, col2, col3 = st.columns(3)

    with col1:

        st.image('FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg',caption ="Lizzy's First Appearance on Camera Roll", width= 200)
        st.image('D677062A-24CD-42AE-80B2-680571D608CE_1_105_c.jpeg', caption="Our First Met Date",
                 width=200)
        st.image('30D16FB5-0810-49BC-AD86-A0816580D0A0_1_105_c.jpeg', caption="Lizzy's First Appearance on Camera Roll",
                 width=200)
    with col2:
        st.image('FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg', caption="Lizzy's First Appearance on Camera Roll",
             width=200)

    with col3:
        st.image('FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg', caption="Lizzy's First Appearance on Camera Roll",
                 width=200)
        st.image('FCF4B0DE-756C-4597-922C-80C18319C316_1_105_c.jpeg', caption="Lizzy's First Appearance on Camera Roll",
             width=200)



with Inside_Jokes:
    st.write('test1')

