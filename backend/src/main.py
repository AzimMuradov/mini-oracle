import os
from typing import Any
from requests import Session
from flask import Flask, request
from backend.src.api import answer_question

app = Flask(__name__)

session = Session()


@app.route("/answers")
def get_answers() -> (list[dict[str, Any]] | dict[str, str]):
    try:
        question_type = request.args.get("question_type", default="", type=str)
        question_content = request.args.get("question_content", default="", type=str)
        return answer_question(question_type, question_content, session)
    except Exception as ex:
        return {"error": f"Error: {ex}"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", default=5000)))
