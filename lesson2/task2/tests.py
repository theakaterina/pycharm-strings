from test_helper import run_common_tests, failed, passed, get_file_output

def test_answer_placeholders():
    answers = get_file_output()
    index = answers[0]
    nemo = answers[1]
    if index == "20":
        passed()
    else:
        failed("Make sure you've used a capital N")
    if nemo == "Nemo":
        passed()
    else:
        failed("Use the wheres_nemo variable to know where to start and end your splice")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()

