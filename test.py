import streamlit as st

st.title('Elizabeth Sarah McNaughton')

container = st.container()

(container.write('test'))

InsideJokes, Memories, Other = st.tabs(["Inside Jokes", "Memories", "Other"])

with InsideJokes:
    st.write('test')

with Memories:
    st.write('test1')

with Other:
    st.write('test4')
