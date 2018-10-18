from typing import Callable

# Return a function which return true - if x parameter is divided by input parameter of returned function - otherwise false
def number_divided_by(x: int) -> Callable:
    def f(input: int) -> bool:
        return input % x == 0
    return f

# Return a function which return true if number has a digit x
def number_has_digit_in_it(x: int) -> Callable:
    def f(input: int) -> bool:
        return bool(any(i == str(x) for i in str(input)))
    return f

# Return a function which return parameter word - when returned function returns true - otherwise empty string
def choose_word(word: str, filter: Callable) -> str:
    def f(input: int) -> str:
        if filter(input) == True:
            return word
        return ""
    return f

# Return a function which returns concatenation of returned values from parameter functions
def compose_and_chain_responsibility(filter1: Callable, filter2: Callable) -> Callable:
    def composer(input: int) -> str:
        return filter1(input) + filter2(input)
    return composer

# Return a function which returns first returned value from parameter functions then breaks the chain
def compose_or_chain_responsibility(filter1: Callable, filter2: Callable) -> Callable:
    def composer(input: int) -> str:
        output1 = filter1(input)
        if (output1 != ""):
            return str(output1)
        return filter2(input)
    return composer

# Return a function which return the result of calling composed_chain_responsibility parameter, otherwise just it's input
def compose_chain_responsibility_with_default_word(composed_chain_responsibility: Callable) -> str:
    def composer(input: int) -> str:
        output = composed_chain_responsibility(input)
        if output != "":
            return output
        return input
    return composer