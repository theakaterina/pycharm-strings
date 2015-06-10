from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    answer = get_file_output()
    if answer[0] == "this is such a long sentence":
        passed()
    else:
        failed("The output should be \"this is such a long sentence\"")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


