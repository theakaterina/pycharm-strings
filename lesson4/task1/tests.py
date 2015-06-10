from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    answers = get_file_output()
    answer = answers[0]
    if answer == "['natasha', 'nautical', 'numbat', 'nitrogen', 'no']":
        passed()
    else:
        failed("You haven't removed all the non-n words")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()