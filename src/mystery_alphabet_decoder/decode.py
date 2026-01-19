"""Decode input assuming the intercepted input represents a known alphabet."""


def iso_639_1(language):
    try:
        return {
            # add more language codes as desired
            'english': 'en',
            'greek': 'el',
        }[language]
    except KeyError as e:
        msg = f"Add '{language}' to the iso_639_1 dictionary"
        raise ValueError(msg) from e


def decode_input(input_file, input_alphabet, output_file, output_alphabet):
    if len(input_alphabet) != len(output_alphabet):
        msg = 'alphabets must have the same length.'
        raise ValueError(msg)
    table = str.maketrans(input_alphabet, output_alphabet)
    with input_file.open('r') as infile, output_file.open('w') as outfile:
        for word in infile:
            outfile.write(word.translate(table))
