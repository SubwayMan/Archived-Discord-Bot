import discord
datasets = {
    'python': {
        'String': [
            '''capitalize() -
            attempts to capitalize the first character of a string.-
            if the first character is not a letter, does nothing
            returns str
            ''',

            '''casefold() -
            similar to lower() except works for non english characters too
            returns str
            ''',

            '''center(length, *character) -
            centers string in whitespace of certain length -
            can specify a character in place of whitespace
            returns str
            ''',

            '''count(value, *start, *end) -
            returns the number of times value occurs in a string-
            can specify the start and end of a substring you wish to search
            returns int
            ''',
            '''encode(*encoding, *error) -
            encodes a string (default is UTF-8) -
            if a character cannot be encoded, *error specifies what to do:
            'backslashreplace'	- uses a backslash instead of the character that could not be encoded
            'ignore' - ignores the characters that cannot be encoded
            'namereplace' - replaces the character with a text explaining the character
            'strict' - Default, raises an error on failure
            'replace' - replaces the character with a questionmark
            'xmlcharrefreplace'	- replaces the character with an xml character
            returns str
            ''',
            '''endswith(substring, *start, *end) -
            returns whether or not a string ends with a certain substring-
            can look at the end of a certain substring if specified
            returns boolean
            '''

        ],
        'List': [

        ],
        'Set': [

        ],
        'Tuple': [

        ],
        'Dict': [

        ],
        'Built_in_functions'
    }
}
