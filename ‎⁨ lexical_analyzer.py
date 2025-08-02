import string

# Global variables
char_class = None
lexeme = []
next_char = ''
lex_len = 0
token = None
next_token = None
in_fp = None

# Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

# Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
EOF = -1

# Function declarations
def add_char():
    global lexeme, lex_len
    if lex_len < 98:
        lexeme.append(next_char)
        lex_len += 1
    else:
        print("Error - lexeme is too long")

def get_char():
    global next_char, char_class
    next_char = in_fp.read(1)
    if next_char == '':
        char_class = EOF
    elif next_char in string.ascii_letters:
        char_class = LETTER
    elif next_char in string.digits:
        char_class = DIGIT
    else:
        char_class = UNKNOWN

def get_non_blank():
    global next_char
    while next_char.isspace():
        get_char()

def lookup(ch):
    global next_token
    if ch == '(':
        add_char()
        next_token = LEFT_PAREN
    elif ch == ')':
        add_char()
        next_token = RIGHT_PAREN
    elif ch == '+':
        add_char()
        next_token = ADD_OP
    elif ch == '-':
        add_char()
        next_token = SUB_OP
    elif ch == '*':
        add_char()
        next_token = MULT_OP
    elif ch == '/':
        add_char()
        next_token = DIV_OP
    else:
        add_char()
        next_token = EOF
    return next_token

def lex():
    global lexeme, lex_len, next_token
    lexeme = []
    lex_len = 0
    get_non_blank()
    if char_class == LETTER:
        add_char()
        get_char()
