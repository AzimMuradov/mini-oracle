import os
from typing import Any
import requests as rq
from backend.src.wiki_api import get_wiki_search_results


def answer_question(
    question_type: str, question_content: str, session: rq.Session
) -> list[dict[str, Any]]:
    try:
        search_results = get_wiki_search_results(question_content, session)
    except ValueError as ex:
        raise RuntimeError(f"Illegal arguments: {ex}")
    except Exception as ex:
        raise RuntimeError(f"Wikipedia error: {ex}")

    def get_answer(title: str, summary: str) -> dict[str, Any]:
        answer = query(
            {
                "question": format_question(question_type, title),
                "context": summary,
            }
        )
        if not isinstance(answer, dict) or "answer" not in answer:
            raise RuntimeError(answer)
        return {"title": title, "answer": answer["answer"].capitalize()}

    return [get_answer(x["title"], x["summary"]) for x in search_results]


def format_question(question_type: str, question_content: str) -> str:
    return (
        f"Who is {question_content}?"
        if question_type == "somebody"
        else f"What is {question_content}?"
    )


def query(payload: dict) -> dict | list:
    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_BEARER_TOKEN')}"}

    response = rq.post(api_url, headers=headers, json=payload)

    return response.json()
