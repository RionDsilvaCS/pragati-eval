import streamlit as st
import os

st.session_state['platforms'] = ("GOOGLE_API_KEY", "GROQ_API_KEY", "OpenAI-comming-soon")

@st.cache_resource
def initialize_session_keys():
    for platform_choice in st.session_state['platforms']:
        if platform_choice not in st.session_state:
            st.session_state[platform_choice] = None
            
st.set_page_config(
    page_title="PragatiEval",
    page_icon="⚖️"
)

st.write("# Welcome to PragatiEval ⚖️")

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
                # st.write(str(f'{platform_choice} API is added'))
                st.sidebar.success(str(f'Added {platform_choice}'))

initialize_session_keys()  