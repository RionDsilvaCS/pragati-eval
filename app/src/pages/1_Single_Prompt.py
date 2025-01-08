import streamlit as st
from utils.model_calls import gemini_model_api, groq_model_api, ollama_model_api

PLATFORMS_DICT = {
    "Google AI Studio":("gemini-1.5-flash", "gemini-1.5-flash-8b", "gemini-1.5-pro", "gemini-2.0-flash-exp"),
    "Groq":("gemma2-9b-it", "llama-3.3-70b-versatile", "llama-3.1-8b-instant", "llama-guard-3-8b", "llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"),
    "OpenAI":("comming-soon"),
    "Ollama":("gemma2:2b", "llama3.2:latest")
    }

PLATFORMS = ("Google AI Studio", "Groq", "OpenAI", "Ollama")

tool_choice = None

@st.cache_resource
def initialize_session_models():
    st.session_state['submit'] = False
    for key, value in PLATFORMS_DICT.items():
        st.session_state[key] = value

def prompt_block(
        id: str ="1", 
        query_prompt: str = "",
        instructions: str = "",
        *,
        tool_name: str | None
    ):

    st.write(f'Batch {id}')

    scol1, scol2 = st.columns(2)

    with scol1:
        platform_choice = st.selectbox(
            str(f'Select platform {id}'),
            PLATFORMS
        )

    with scol2:
        mode_choice = st.radio(
            str(f'Select mode {id}'),
            ("list id's", "custom id"),
            horizontal=True
        )

    if mode_choice == "list id's":
        model_id = st.selectbox(
            str(f'Select model {id}'),
            st.session_state[platform_choice]
        )
    elif mode_choice == "custom id":
        model_id = st.text_input(
            str(f'Model {id}'),
        )

    if st.session_state['submit']:
        if query_prompt != "":

            if platform_choice == "Google AI Studio":
                try:
                    model_response, latency = gemini_model_api(model_id=model_id, query_prompt=query_prompt, instructions=instructions, tool_name=tool_name)
                except Exception as e:
                    model_response = e

            if platform_choice == "Groq":
                try:
                    model_response, latency = groq_model_api(model_id=model_id, query_prompt=query_prompt, instructions=instructions, tool_name=tool_name)
                except Exception as e:
                    model_response = e

            if platform_choice == "Ollama":
                try:
                    model_response, latency = ollama_model_api(model_id=model_id, query_prompt=query_prompt, instructions=instructions, tool_name=tool_name)
                except Exception as e:
                    model_response = e
            
            st.write(f'Platform latency : {latency} ms')

            st.markdown("---")
            
            st.markdown(model_response)
    else:
        st.markdown("---")
        st.markdown("*Your response will here*")

st.set_page_config(
    page_title="Single Prompt",
    page_icon="⚖️",
    layout="wide"
)

st.write("## Single Prompt Eval ⚖️")

initialize_session_models()

col_1, col_2 = st.columns(2)

with col_1:
    number_of_instances = st.selectbox(
        "Number of Instances",
        (1, 2, 3, 4),
    )

with col_2:
    task_choice = st.selectbox(
        "Select test type",
        ("Query Test", "DataStore Test", "Tool Test"),
    )

user_prompt = st.text_area("Query prompt 👇", placeholder="query prompt here ...")
 
instruction_prompt = st.text_area("Instruction prompt 👇", placeholder="instruction prompt here ...")

if task_choice == "Tool Test":
    tool_choice = st.selectbox(
        "Select tool",
        ("DuckDuckGo", "Arxiv tool", "YFinance tool"),
    )

if st.button("Submit"):
    st.session_state['submit'] = True
else:
    # if 'submit' not in st.session_state:
    st.session_state['submit'] = False

if number_of_instances == 2:
    col1, col2 = st.columns(2)
    with col1:
        prompt_block(query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
    
    with col2:
        prompt_block(id="2",query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)


elif number_of_instances == 3:
    col1, col2, col3 = st.columns(3)
    with col1:
        prompt_block(query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
    
    with col2:
        prompt_block(id="2", query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
        
    with col3:
        prompt_block(id="3", query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)


elif number_of_instances == 4:
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        prompt_block(query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
    
    with col2:
        prompt_block(id="2", query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
        
    with col3:
        prompt_block(id="3", query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
    
    with col4:
        prompt_block(id="4", query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)

else:
    prompt_block(query_prompt=user_prompt, instructions=instruction_prompt, tool_name=tool_choice)
    
