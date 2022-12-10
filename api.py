from transformers import pipeline

from wikipedia_api import get_wiki_stats

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


def answer_question(content, question_type):
    # a) Get predictions
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

    wiki_stats = get_wiki_stats(content)

    def transform_stat(title, context):
        answer = nlp({
            'question': format_question_type(question_type).replace('_', content),
            'context': context
        })['answer']
        return title, answer

    return [transform_stat(x[0], x[1]) for x in wiki_stats]
