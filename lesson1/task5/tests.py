from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if placeholder == "lyric1 + lyric2 + lyric3":
        passed()
    else:
        failed("Remember to use + to join the words")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


