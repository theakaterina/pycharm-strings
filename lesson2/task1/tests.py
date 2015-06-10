from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    answers = get_file_output()
    mississippi = answers[0]
    flies = answers[1]
    if mississippi == "There are 4 i's in mississippi":
        passed()
    else:
        failed("Something is wrong with the mississippi count")
    if flies == "There are 2 flies in that sentence":
        passed()
    else:
        failed("Something is wrong with the number of flies")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


