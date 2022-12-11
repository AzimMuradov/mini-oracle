from backend.src.api import format_question_type


def test_format_question_type_somebody() -> str:
    assert "Who is _?" == format_question_type("somebody")


def test_format_question_type_something() -> str:
    assert "What is _?" == format_question_type("something")


def test_format_question_type_else() -> str:
    assert "What is _?" == format_question_type("dfsazdf")
