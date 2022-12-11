import requests
import streamlit as st

session = requests.Session()

question_types = ['somebody', 'something']


def format_question_type(question_type):
    match question_type:
        case 'somebody':
            formatted_question_type = 'Who is _?'
        case 'something':
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

    url = "https://mini-oracle.up.railway.app/answers"
    params = {"question_type": q_type, "question_content": q_content}

    if submitted:
        answers = session.get(url=url, params=params).json()
        if isinstance(answers, list):
            for line in [format_res(x['title'], x['answer']) for x in answers.json()]:
                st.text(line)
        else:
            st.text(answers['error'])
