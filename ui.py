import streamlit as st
import pandas as pd
from chatbot import query_agent

#type=["*.csv, *xlsx"]


def navigation():
    st.title("DEEP WRANGLER")
    st.text("Ask this bot questions about your data.")
    with st.expander("**Upload data**"):
        st.header("Upload your data")
        uploaded_file = st.file_uploader("Upload file", accept_multiple_files=False, \
                                          help="Click the browse \
                                            files button to upload a file.Accepted files are csv or excel files\
                                        ")
        
        if uploaded_file:
            st.info(f" You uploaded {uploaded_file.name}")
            if uploaded_file.name.split(".")[1] == "csv":
                dataframe = pd.read_csv(uploaded_file)
            elif uploaded_file.name.split(".")[1] == "xlsx":
                dataframe = pd.read_excel(uploaded_file)
            st.write(dataframe)

    with st.expander("**Question your data**"):
        question = st.text_input("Type your question here")
        if question:
            st.info(query_agent(dataframe, question))


     
            
navigation()