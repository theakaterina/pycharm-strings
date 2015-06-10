from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    answers = get_file_output()
    hey_jude = answers[0]
    batman = answers[1]
    if hey_jude == "na na na na na na na na na hey jude":
        passed()
    else:
        failed("Something wrong hey jude")
    if batman == "na na na na na na na na na na na na na na na na batman":
        passed()
    else:
        failed("Something wrong with batman")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call


