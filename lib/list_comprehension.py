#!/usr/bin/env python3
def return_evens(num_list):
    """Return a list of even numbers from the given list."""
    return [n for n in num_list if n % 2 == 0]


def make_exclamation(sentences):
    """Return a list of sentences with an exclamation mark at the end."""
    return [sentence + "!" for sentence in sentences]
