import streamlit as st
import pandas as pd
import io

def display_Master_Spreadsheet_panel():
    st.title("Master Data Upload")

    # Initialize session state for master_df and raw_file
    if "master_df" not in st.session_state:
        st.session_state["master_df"] = None
    if "raw_file" not in st.session_state:
        st.session_state["raw_file"] = None

    # File Uploader
    uploaded_file = st.file_uploader("Upload the master CSV file:", type="csv")

    if uploaded_file is not None:
        # Save raw file contents to session_state
        st.session_state["raw_file"] = uploaded_file.getvalue()
        st.session_state["master_df"] = pd.read_csv(io.BytesIO(st.session_state["raw_file"]))
        st.success("Master data loaded!")

    # Check if data exists in session_state
    if st.session_state["master_df"] is not None:
        master_df = st.session_state["master_df"]
        st.dataframe(master_df)
    else:
        st.warning("Please upload a CSV file.")
