"""Deduce the order of a mystery alphabet."""

from collections import defaultdict
from itertools import pairwise


def deduce_alphabet_order(input_file):
    """Deduce the order of a mystery alphabet.

    Args:
        input_file (Path): a file containing an intercepted dictionary snippet with
        letters encoded by mystery symbols.

    Returns:
        A string of symbols in mystery alphabetical order.

    """
    # Build a graph of symbol relationships.
    # This is a dictionary with the following format:
    #   key: a letter in the mystery script (e.g. '⊛')
    #   value: a set containing letters known to occur BEFORE this letter
    graph = defaultdict(set)
    with input_file.open('r') as file:
        for word1, word2 in pairwise(file):
            for letter1, letter2 in zip(word1.strip(), word2.strip(), strict=False):
                if letter1 != letter2:
                    # this is the first position where word1 and word2 differ
                    # mark letter1 as occuring before letter2
                    if letter2 in graph[letter1]:
                        msg = f"There is a logical contradiction in '{input_file}'"
                        raise ValueError(msg)
                    graph[letter2].add(letter1)
                    break

    # Iteratively search the graph to find the next letter.
    # The next letter is the letter that has no letters that occur before it except
    # those that have already been added to the alphabet.
    alphabet = []
    while len(graph):
        next_letter_candidates = [
            letter
            for (letter, letters_that_occur_before) in graph.items()
            if len(letters_that_occur_before) == 0
        ]
        if len(next_letter_candidates) == 1:
            next_letter = next_letter_candidates[0]
            alphabet.append(next_letter)
            del graph[next_letter]
            for letter in graph:
                graph[letter].discard(next_letter)
        elif len(next_letter_candidates) == 0:
            msg = f"There is a logical contradiction in '{input_file}'"
            raise ValueError(msg)
        else:
            msg = (
                f"'{input_file}' does not contain sufficient information to determine"
                'a unique alphabetical order.'
            )
            raise ValueError(msg)

    return ''.join(alphabet)

if __name__ == '__main__':
    from pathlib import Path
    infile = Path() / 'input.txt'
    print(deduce_alphabet_order(infile)) #noqa: T201
