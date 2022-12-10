from transformers import pipeline

from wiki_api import get_wiki_search_results

model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"

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


def answer_question(question_type, question_content, session):
    # a) Get predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    search_results = get_wiki_search_results(question_content, session)

    def get_answer(title, summary):
        answer = nlp({
            'question': format_question_type(question_type).replace('_', title),
            'context': summary
        })['answer']
        return {'title': title, 'answer': answer.capitalize()}

    return [get_answer(x['title'], x['summary']) for x in search_results]
