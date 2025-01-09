import streamlit as st
import os

st.session_state['platforms'] = ("GOOGLE_API_KEY", "GROQ_API_KEY", "OpenAI-comming-soon")

@st.cache_resource
def initialize_session_keys():
    for platform_choice in st.session_state['platforms']:
        if platform_choice not in st.session_state:
            st.session_state[platform_choice] = None
       
st.set_page_config(
    page_title="Pragati Eval",
    page_icon="😎"
)

st.write("# Welcome to Pragati Eval 😎")

st.write("A free and open-source platform designed to help developers, especially those new to AI, easily evaluate the performance of different Large Language Models (LLMs) for their specific use cases. Inspired by Maxim AI, Pragati Eval offers a user-friendly interface for streamlined LLM experimentation.")

st.image("https://i.ibb.co/hVgQjDZ/hero-pic.jpg")

platform_choice = st.sidebar.selectbox(
    "Select model platform",
    st.session_state['platforms']
)

with st.sidebar:
    model_api_key = st.text_input("API KEY", type='password', placeholder="API KEY here XXXX")

    if st.button("Add"):
        st.session_state[platform_choice] = model_api_key
        os.environ[platform_choice] = model_api_key
        
    for platform_choice in st.session_state['platforms']:   
        if platform_choice in st.session_state:
            if st.session_state[platform_choice] is not None:
                st.sidebar.success(str(f'Added {platform_choice}'))

initialize_session_keys()  