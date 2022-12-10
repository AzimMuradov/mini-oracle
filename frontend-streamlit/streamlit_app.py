import requests
import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

session = requests.Session()

question_types = ['smbdy', 'smthg']


def format_question_type(question_type):
    match question_type:
        case 'smbdy':
            formatted_question_type = 'Who is _?'
        case 'smthg':
            formatted_question_type = 'What is _?'
        case _:
            formatted_question_type = 'What is _?'
    return formatted_question_type


def format_res(title, answer):
    return f"{format_question_type(q_type).replace('_', title)} -- {answer}"


with st.form("main_form"):
    q_type = st.selectbox("Type of the question", question_types, format_func=format_question_type)
    q_content = st.text_input("Question content", max_chars=50, placeholder="Machine learning")
    submitted = st.form_submit_button("Submit")

    url = "https://mini-oracle-production.up.railway.app/"
    params = {"question_type": q_type, "question_content": q_content}

    if submitted:
        answers = session.get(url=url, params=params).json()
        for line in [format_res(x['title'], x['answer']) for x in answers]:
            st.text(line)
