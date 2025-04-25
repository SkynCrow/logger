class ANSII:
    # Reset
    RESET = "\x1b[0m"

    # Colores regulares
    BLACK = "\x1b[30;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    BLUE = "\x1b[34;20m"
    MAGENTA = "\x1b[35;20m"
    CYAN = "\x1b[36;20m"
    WHITE = "\x1b[37;20m"

    # Colores claros
    BRIGHT_BLACK = "\x1b[30;1m"
    BRIGHT_RED = "\x1b[31;1m"
    BRIGHT_GREEN = "\x1b[32;1m"
    BRIGHT_YELLOW = "\x1b[33;1m"
    BRIGHT_BLUE = "\x1b[34;1m"
    BRIGHT_MAGENTA = "\x1b[35;1m"
    BRIGHT_CYAN = "\x1b[36;1m"
    BRIGHT_WHITE = "\x1b[37;1m"

    # Otros
    GREY = "\x1b[38;20m"
    DARK_GREY = "\x1b[38;5;236m"
    LIGHT_GREY = "\x1b[38;5;251m"
    ORANGE = "\x1b[38;5;208m"
    PURPLE = "\x1b[38;5;141m"
    TEAL = "\x1b[38;5;31m"
    LIME = "\x1b[38;5;154m"
    PINK = "\x1b[38;5;213m"
    LAVENDER = "\x1b[38;5;183m"
    SKY_BLUE = "\x1b[38;5;111m"
    
    # Colores de fondo
    BG_BLACK = "\x1b[40m"
    BG_RED = "\x1b[41m"
    BG_GREEN = "\x1b[42m"
    BG_YELLOW = "\x1b[43m"
    BG_BLUE = "\x1b[44m"
    BG_MAGENTA = "\x1b[45m"
    BG_CYAN = "\x1b[46m"
    BG_WHITE = "\x1b[47m"
    BG_DEFAULT = "\x1b[49m"
    
    # Colores de fondo (brillantes)
    BG_BRIGHT_BLACK = "\x1b[100m"
    BG_BRIGHT_RED = "\x1b[101m"
    BG_BRIGHT_GREEN = "\x1b[102m"
    BG_BRIGHT_YELLOW = "\x1b[103m"
    BG_BRIGHT_BLUE = "\x1b[104m"
    BG_BRIGHT_MAGENTA = "\x1b[105m"
    BG_BRIGHT_CYAN = "\x1b[106m"
    BG_BRIGHT_WHITE = "\x1b[107m"
    
    #Formato de texto
    BOLD = "\x1b[1m"
    DIM = "\x1b[2m"
    ITALIC = "\x1b[3m"   #No funciona en todos los terminales
    UNDERLINE = "\x1b[4m"
    BLINK = "\x1b[5m"
    FAST_BLINK = "\x1b[6m"   #No funciona en todos los terminales
    REVERSED = "\x1b[7m"
    HIDDEN = "\x1b[8m"
    STRIKETHROUGH = "\x1b[9m"
    
    # Cancelar formato
    RESET_BOLD_DIM = "\x1b[22m"
    RESET_ITALIC = "\x1b[23m"
    RESET_UNDERLINE = "\x1b[24m"
    RESET_BLINK = "\x1b[25m"
    RESET_REVERSED = "\x1b[27m"
    RESET_HIDDEN = "\x1b[28m"
    RESET_STRIKETHROUGH = "\x1b[29m"
    
    CHARS = {
        "t": "═",
        "b": "═",
        "r": "║",
        "l": "║",
        "tr": "╗",
        "tl": "╔",
        "br": "╝",
        "bl": "╚",
        "c": "╬",
        "ct": "╦",
        "cb": "╩",
        "cl": "╠",
        "cr": "╣",
}