"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

from collections import Counter


def generate_phrase(characters, phrase):
    character_count = Counter(characters.lower())
    phrase_count = Counter(phrase.lower())
    if len(characters) < len(phrase):
        return False
    for i, count in phrase_count.items():
        if i in character_count and count <= character_count.get(i):
            return True
        else:
            return False


if __name__ == "__main__":
    print(generate_phrase("cbacba", "aabbccc"))  # Should show False
    print(generate_phrase("cbacbac", "aabbccc"))  # Should show True
    print(generate_phrase("monkey", "bananas"))  # Should show False
    print(generate_phrase("sabnanabas", "bananas"))  # Should show True
