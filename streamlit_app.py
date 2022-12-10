import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

from api import question_types, answer_question, model_name, format_question_type

# TODO : Docs

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def format_res(title, answer):
    return f"{format_question_type(question_type).replace('_', title)} -- {answer}"


with st.form("main_form"):
    question_type = st.selectbox("Type of the question", question_types, format_func=format_question_type)
    question_content = st.text_input("Question content", max_chars=50, placeholder="Machine learning")
    submitted = st.form_submit_button("Submit")

    if submitted:
        res = answer_question(question_content, question_type)
        for line in [format_res(x[0], x[1]) for x in res]:
            st.text(line)
