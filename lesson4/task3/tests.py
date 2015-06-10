from test_helper import run_common_tests, failed, passed, get_file_output


def test_answer_placeholders():
    placeholders = get_file_output()
    link1 = placeholders[0]
    link2 = placeholders[1]
    link3 = placeholders[2]
    if link1 == "https://www.youtube.com/watch?v=Voa9QwiBJwE#t=8m57s":
        passed()
    else:
        failed("Are you only returning youtube links?")

    if link2 == "https://www.youtube.com/watch?v=jluQyS4lFpY":
        passed()
    else:
        failed("Are you only returning youtube links?")

    if link3 == "https://www.youtube.com/watch?v=PrI2oXDTanI":
        passed()
    else:
        failed("Are you only returning youtube links?")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()