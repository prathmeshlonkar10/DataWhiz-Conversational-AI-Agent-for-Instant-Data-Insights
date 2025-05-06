# ========== CODE START ========== #

# Importing libraries
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Setting Streamlit UI
st.set_page_config(layout="wide")
st.title("Welcome to DataWhiz!🧩")
st.subheader("Conversations With Data, Made Simple!! 💬")
st.divider()

# ========== FUNCTIONS START ========== #

def process_file_upload(uploaded_file):
    if uploaded_file is not None:
        # Read the CSV dataset to be converted into dataframe.
        df = pd.read_csv(uploaded_file)
        #st.toast("CSV file uploaded successfully!", icon="✅")
        return df
    else:
        st.session_state.file_upload = False
        return None

def upload_state_update():   
    try:
        # State for consecutive uploads.
        st.session_state.file_upload = True
    except:
        # Initializing the file upload state.
        if "file_upload" not in st.session_state:
            st.session_state.file_upload = True

def create_agent(df):
    # Setting OpenAI model.
    model = "gpt-4o-mini"

    # Setting OpenAI API key.
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Setting the LLM.
    llm = ChatOpenAI(model=model, temperature=0)

    # Setting the Agent type.
    agent_type = AgentType.OPENAI_FUNCTIONS

    # Setting the Agent to interact with Dataframe.
    df_agent = create_pandas_dataframe_agent(
        llm=llm, 
        df=df, 
        agent_type=agent_type,
        suffix="Also return a JSON dictionary that can be parsed into a dataframe containing the requested information",
        verbose=True,
        allow_dangerous_code=True)

    return df_agent

# ========== FUNCTIONS END ========== #

# Layout with two columns.
col1, col2 = st.columns([1, 1], gap="large")

# Uploading CSV from user.
with col1:
    uploaded_file = st.file_uploader(
        label = "Let's unlock insights from your data! Please upload your CSV file here to proceeed ⚡", 
        type = ["csv"], 
        help = "Supported format: .csv",
        on_change = upload_state_update)

    # Post-upload activities. 
    if "file_upload" in st.session_state:
        if st.session_state.file_upload:
            df = process_file_upload(uploaded_file)

            if df is not None:
                # Display Dataframe on UI.
                st.divider()
                st.dataframe(df, use_container_width=True)

                df_agent = create_agent(df)

                with col2:
                    # Heading for Chat window.
                    st.subheader("💬 Chat with Your Data")

                    # Container for chat window.
                    chat_window = st.container(height=530)

                    # Initializing chat history.
                    if "chat_history" not in st.session_state:
                        st.session_state.chat_history = []
                    
                    # Displaying prior chat messages from history upon app rerun (new prompt input).
                    for message in st.session_state.chat_history:
                        chat_window.chat_message(message["role"]).markdown(message["content"])
                    
                    # Accepting user input.
                    if prompt := st.chat_input("Ask a question to know your data better..."):
                        # Adding user message to chat history.       
                        st.session_state.chat_history.append({"role": "user", "content": prompt})

                        # Displaying user message in chat message container.
                        chat_window.chat_message("user").markdown(prompt)

                        with st.spinner("🔎 Analyzing your data, please wait..."): 
                            try:                      
                                # Displaying assistant response in chat message container.
                                response = df_agent.invoke(prompt)["output"]
                                chat_window.chat_message("assistant").write(response)

                                # Adding assistant response to chat history.
                                st.session_state.chat_history.append({"role": "assistant", "content": response})
                            except Exception as e:
                                st.error(f"⚠️ Oops! Something went wrong: {str(e)}")
            else:
                st.warning("⚠️ Please upload a CSV file to start exploring your data.")
                if "chat_history" in st.session_state:
                    st.session_state.chat_history = []

# Footer
st.divider()
st.caption("<center>💼 Powered by Langchain and Streamlit — Simplifying Data Insights</center>", unsafe_allow_html=True)

# ========== CODE END ========== #