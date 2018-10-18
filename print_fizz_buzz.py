from fizz_buzz.fizz_buzz import \
    number_divided_by, \
    number_has_digit_in_it, \
    choose_word, \
    compose_and_chain_responsibility,\
    compose_or_chain_responsibility, \
    compose_chain_responsibility_with_default_word

# Prints fizz buzz example
def print_fizz_buzz():

    d = number_divided_by(7)
    print(d(15))

    d = number_divided_by(3)
    print(d(9))


    return

    # Has three or is devided by three
    divided_by_three = choose_word("Fizz", number_divided_by(3))
    has_three_in_it = choose_word("Fizz", number_has_digit_in_it(3))
    divided_by_three_or_has_three_in_it = compose_or_chain_responsibility(divided_by_three, has_three_in_it)

    # Has five or is devided by five
    divided_by_five = choose_word("Buzz", number_divided_by(5))
    has_five_in_it = choose_word("Buzz", number_has_digit_in_it(5))
    divided_by_five_or_has_five_in_it = compose_or_chain_responsibility(divided_by_five, has_five_in_it)

    # Has three or is devided by three and Has five or is devided by five
    chain_responsibility = compose_and_chain_responsibility(divided_by_three_or_has_three_in_it, divided_by_five_or_has_five_in_it)
    chain_responsibility_with_default_word = compose_chain_responsibility_with_default_word(chain_responsibility)

    for i in range(1, 100):
        print(chain_responsibility_with_default_word(i))


print_fizz_buzz()