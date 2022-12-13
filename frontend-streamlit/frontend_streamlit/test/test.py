from frontend_streamlit.src.main import format_question_type, format_res


def test_format_question_type_somebody():
    assert "Who is _?" == format_question_type("somebody")


def test_format_question_type_something():
    assert "What is _?" == format_question_type("something")


def test_format_question_type_else():
    assert "What is _?" == format_question_type("...")


def test_format_res_somebody():
    assert "Who is Mr. Putin? -- censored" == format_res("somebody", "Mr. Putin", "censored")


def test_format_res_something():
    assert "What is Love? -- Oh baby, don't hurt me..." == format_res("something", "Love", "Oh baby, don't hurt me...")


def test_format_res_else():
    assert "What is Life? -- 42" == format_res("...", "Life", "42")
