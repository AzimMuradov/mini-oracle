import requests
import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

from api import question_types, answer_question, model_name, format_question_type

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

session = requests.Session()


def format_res(title, answer):
    return f"{format_question_type(question_type).replace('_', title)} -- {answer}"


with st.form("main_form"):
    question_type = st.selectbox("Type of the question", question_types, format_func=format_question_type)
    question_content = st.text_input("Question content", max_chars=50, placeholder="Machine learning")
    submitted = st.form_submit_button("Submit")

    if submitted:
        answers = answer_question(question_type, question_content, session)
        for line in [format_res(x['title'], x['answer']) for x in answers]:
            st.text(line)
