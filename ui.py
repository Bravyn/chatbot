import streamlit as st
import pandas as pd


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
            uploaded_file = pd.read_csv(uploaded_file)
            st.write(uploaded_file)

        


        
            
navigation()