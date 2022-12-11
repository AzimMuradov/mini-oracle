from frontend_streamlit.src.main import format_question_type, format_res


def test_format_question_type_somebody() -> str:
    assert "Who is _?" == format_question_type("somebody")


def test_format_question_type_something() -> str:
    assert "What is _?" == format_question_type("something")


def test_format_question_type_else() -> str:
    assert "What is _?" == format_question_type("dfsazdf")


def test_format_res_somebody() -> str:
    assert "Who is Mr. Putin? -- censored" == format_res("somebody", "Mr. Putin", "censored")


def test_format_res_something() -> str:
    assert "What is Love? -- Oh baby, don't hurt me..." == format_res("something", "Love", "Oh baby, don't hurt me...")


def test_format_res_else() -> str:
    assert "What is Life? -- 42" == format_res("...", "Life", "42")
