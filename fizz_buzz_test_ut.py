import unittest

from fizz_buzz.fizz_buzz import \
    number_divided_by, \
    choose_word, \
    compose_or_chain_responsibility,\
    compose_and_chain_responsibility,\
    number_has_digit_in_it,\
    compose_chain_responsibility_with_default_word

class TestCalcPriceForBooks(unittest.TestCase):

    def test_number_divided_by(self):
        divided_by_three = number_divided_by(3)
        self.assertTrue(divided_by_three(9))
        self.assertFalse(divided_by_three(8))

        divided_by_five = number_divided_by(5)
        self.assertTrue(divided_by_five(10))
        self.assertFalse(divided_by_five(9))

    def test_number_has_digit_in_it(self):
        has_tree_in_it = number_has_digit_in_it(3)
        self.assertTrue(has_tree_in_it(3))
        self.assertTrue(has_tree_in_it(13))

    def test_choose_word(self):
        divided_by_three = number_divided_by(3)
        say_fizz = choose_word("fizz", divided_by_three)
        self.assertEqual(say_fizz(3), "fizz")
        self.assertEqual(say_fizz(4), "")

    def test_compose_chain_responsibility_with_default_word(self):
        divided_by_three = choose_word("Fizz", number_divided_by(3))
        has_three_in_it = choose_word("Fizz", number_has_digit_in_it(3))
        divided_by_three_or_has_three_in_it = compose_or_chain_responsibility(divided_by_three, has_three_in_it)

        divided_by_five = choose_word("Buzz", number_divided_by(5))
        has_five_in_it = choose_word("Buzz", number_has_digit_in_it(5))
        divided_by_five_or_has_five_in_it = compose_or_chain_responsibility(divided_by_five, has_five_in_it)

        chain_responsibility = compose_and_chain_responsibility(divided_by_three_or_has_three_in_it, divided_by_five_or_has_five_in_it)
        chain_responsibility_with_default_word = compose_chain_responsibility_with_default_word(chain_responsibility)

        self.assertEqual(chain_responsibility_with_default_word(3), "Fizz")
        self.assertEqual(chain_responsibility_with_default_word(5), "Buzz")
        self.assertEqual(chain_responsibility_with_default_word(15), "FizzBuzz")
        self.assertEqual(chain_responsibility_with_default_word(14), 14)
        self.assertEqual(chain_responsibility_with_default_word(31), "Fizz")
        self.assertEqual(chain_responsibility_with_default_word(53), "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
