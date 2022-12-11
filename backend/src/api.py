import os
import requests
from wiki_api import get_wiki_search_results


def answer_question(question_type, question_content, session):
    try:
        search_results = get_wiki_search_results(question_content, session)
    except ValueError as ex:
        return RuntimeError(f"Illegal arguments: {ex}")
    except Exception as ex:
        return RuntimeError(f"Wikipedia error: {ex}")

    def get_answer(title, summary):
        answer = query({
            'question': format_question_type(question_type).replace('_', title),
            'context': summary
        })
        if not isinstance(answer, dict) or 'answer' not in answer:
            raise RuntimeError(answer)
        return {'title': title, 'answer': answer.capitalize()}

    return [get_answer(x['title'], x['summary']) for x in search_results]


def format_question_type(question_type):
    match question_type:
        case 'somebody':
            formatted_question_type = 'Who is _?'
        case 'something':
            formatted_question_type = 'What is _?'
        case _:
            formatted_question_type = 'What is _?'
    return formatted_question_type


def query(payload):
    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {os.getenv('HUGGING_FACE_BEARER_TOKEN')}"}

    response = requests.post(api_url, headers=headers, json=payload)

    return response.json()
