from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0].strip("\"\'") == "mmmm i love onions":
        passed()
    else:
        failed("Something is wrong with answer1")
    if placeholders[1].strip("\"\'") == "i love onions":
        passed()
    else:
        failed("Something is wrong with answer2")
    if placeholders[2].strip("\"\'") == "cbababcaba":
        passed()
    else:
        failed("Something is wrong with answer3")
    if placeholders[3].strip("\"\'") == "abbbabcbababc":
        passed()
    else:
        failed("Something is wrong with answer4")
    if placeholders[4].strip("\"\'") == "":
        passed()
    else:
        failed("Something is wrong with answer5")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()