from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    answers = get_file_output()
    answer = answers[0]
    if answer == "['google', 'facebook', 'youtube', 'amazon', 'twitter', 'ebay', 'reddit']":
        passed()
    else:
        failed("Did you remove the last entry (blank)?")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


