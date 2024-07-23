import streamlit as st
import pandas as pd
from chatbot import query_agent

#type=["*.csv, *xlsx"]
dataa = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "sales": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

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
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)

    with st.expander("**Question your data**"):
        question = st.text_input("Type your question here")
        if question:
            st.info(query_agent(dataframe, question))


     
            
navigation()