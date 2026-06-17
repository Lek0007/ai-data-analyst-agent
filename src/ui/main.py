import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, PROJECT_ROOT)

from app.query_engine import process_question

st.set_page_config(
    page_title="Autonomous Data Analyst",
    layout="wide"
)

st.title("🤖 Autonomous Data Analyst")

question = st.text_input(
    "Ask a business question"
)

if question:

    with st.spinner("Analyzing..."):

        result = process_question(
            question
        )

    st.subheader("Generated SQL")

    st.code(
        result["sql"],
        language="sql"
    )

    st.subheader("Results")

    st.dataframe(
        result["df"]
    )

    st.subheader("Business Insights")

    st.write(
        result["insights"]
    )

    st.write(
        f"Execution Time: {result['execution_time']} sec"
    )