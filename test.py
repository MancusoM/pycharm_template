import streamlit as st

st.title('Elizabeth Sarah McNaughton')

container = st.container()

(container.write('test'))

InsideJokes, Memories, Other = st.tabs(["Inside Jokes", "Memories", "Other"])

with InsideJokes:
    st.write('test')

    UnhingedThingsSFW,UnhingedThingsNSFW = st.tabs(['Unhinged Things Elizabeth has told me (SFW)','Unhinged Things Elizabeth has told me (NSFW)'])

    with UnhingedThingsSFW:
        st.write('test')

        col1 =st.columns(1)

    with UnhingedThingsNSFW:
        st.write('test1')
with Memories:
    st.write('test1')

with Other:
    st.write('test4')
