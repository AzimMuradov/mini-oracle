from backend.src.api import format_question


def test_format_question_somebody():
    assert "Who is Alice?" == format_question("somebody", "Alice")


def test_format_question_something():
    assert "What is Haskell?" == format_question("something", "Haskell")


def test_format_question_else():
    assert "What is Python?" == format_question("...", "Python")
