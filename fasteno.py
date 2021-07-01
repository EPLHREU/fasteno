from plover.system.english_stenotype import *

KEYS = ('C-', 'B-', 'L-', 'F-', 'S-', 'N-', 'T-', 'H-', 'M-', 'G-',
        'I', 'E', 'O',
        '-Z', '-T', '-N', '-A', '-S', '-@', '-F', '-R', '-D', '-$')

IMPLICIT_HYPHEN_KEYS = ('I', 'E', 'O')
SUFFIX_KEYS = ()
NUMBERS = {}
NUMBER_KEY = None
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_WORDLIST = None
ORTHOGRAPHY_RULES_ALIASES = {}

KEYMAPS = {
 'Keyboard': {
        'C-'        : 'q',
        'B-'        : 'a',
        'L-'        : 'w',
        'F-'        : 's',
        'S-'        : 'e',
        'N-'        : 'd',
        'T-'        : 'r',
        'H-'        : 'f',
        'M-'        : 't',
        'G-'        : 'g',
        'I'         : 'v',
        'E'         : 'b',
        'O'         : 'n',
        '-Z'        : 'y',
        '-T'        : 'h',
        '-N'        : 'u',
        '-A'        : 'j',
        '-S'        : 'i',
        '-@'        : 'k',
        '-F'        : 'o',
        '-R'        : 'l',
        '-D'        : 'p',
        '-$'        : ';',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'c', 'm', ',', '.')
    }
}
