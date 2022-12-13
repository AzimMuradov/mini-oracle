import requests
import streamlit as st

session = requests.Session()

question_types = ["somebody", "something"]


def format_question_type(question_type: str) -> str:
    return "Who is _?" if question_type == "somebody" else "What is _?"


def format_res(question_type: str, title: str, answer: str) -> str:
    return f"{format_question_type(question_type).replace('_', title)} -- {answer}"


with st.form("main_form"):
    q_type = st.selectbox("Type of the question", question_types, format_func=format_question_type)
    if not q_type:
        raise RuntimeError("Streamlit error")
    q_content = st.text_input("Question content", max_chars=50, placeholder="Machine learning")
    submitted = st.form_submit_button("Submit")

    url = "https://mini-oracle.up.railway.app/answers"
    params = {"question_type": q_type, "question_content": q_content}

    if submitted:
        answers = session.get(url=url, params=params).json()
        if isinstance(answers, list):
            if not answers:
                st.text("👽   No answers found...")
            else:
                for line in [format_res(q_type, x["title"], x["answer"]) for x in answers]:
                    st.text(f"✅   {line}")
        else:
            st.text(f"❌   {answers['error']}")
