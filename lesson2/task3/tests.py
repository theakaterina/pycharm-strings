from test_helper import run_common_tests, failed, passed, get_file_output


def check_answers():
    answers = get_file_output()
    t_rex1 = answers[0]
    t_rex2 = answers[1]
    t_rex3 = answers[2]
    t_rex4 = answers[5]
    t_rex5 = answers[8]
    if t_rex1 == "In today's society, knowing a little about computers can go a long way!":
        passed()
    else:
        failed("First line is not correct")

    if t_rex2 == "They're not magic boxes. In fact, the more you learn about them the less magical they'll be!":
        passed()
    else:
        failed("Second line is not correct - did you just capitalize the first sentence?")

    if t_rex3 == "Soon you'll be staring at an obscure compiler error and no magic will be left in the world!":
        passed()
    else:
        failed("Third line is not correct")

    if t_rex4 == "I thought I'd actually start with logic gates, and build up to simple machine languages from that?":
        passed()
    else:
        failed("Sixth line is not correct - is I'd written correctly?")

    if t_rex5 == "NO, DON'T SAY THAT!":
        passed()
    else:
        failed("Last line not correct - is it all uppercase?")


if __name__ == '__main__':
    run_common_tests()
    check_answers()

