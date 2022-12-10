import os

import requests
from flask import Flask, request

from api import answer_question

app = Flask(__name__)

session = requests.Session()


@app.route("/answers")
def get_answers():
    question_type = request.args.get('question_type', default="", type=str)
    question_content = request.args.get('question_content', default="", type=str)
    # answers = answer_question(question_type, question_content, session)
    return {'question_type': question_type, 'question_content': question_content}

# model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv("PORT", default=5000))
