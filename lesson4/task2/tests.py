from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    placeholders = get_file_output()
    placeholder = placeholders[0]
    if placeholder == "oh my goodness a secret message":
        passed()
    else:
        failed("You should only have the digits removed.")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()