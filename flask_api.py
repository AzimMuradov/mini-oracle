import requests
from flask import Flask, request

from api import answer_question

app = Flask(__name__)

session = requests.Session()


@app.route("/answers")
def get_answers():
    question_type = request.args.get('question_type', default="sdfsdf", type=str)
    question_content = request.args.get('question_content', default=" ssdf sdfs", type=str)
    answers = answer_question(question_type, question_content, session)
    return answers


if __name__ == "__main__":
    app.run()
